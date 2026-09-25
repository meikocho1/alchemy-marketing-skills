"""Train one skill's SKILL.md with SkillOpt (https://github.com/microsoft/SkillOpt).

Usage, with SkillOpt cloned next to this repo and installed editable
(`pip install -e .`; the base config lives in the checkout, not the package):

    ../SkillOpt/.venv/bin/python optimize/train.py reframing [skillopt-train options]

The target model answers each prompt in skills/<name>/evals/evals.json with the
SKILL.md as its system prompt. The optimizer model then judges every assertion:
soft = share of assertions met, hard = all met. Results, including the split
used and best_skill.md, land in optimize/runs/<name>/<timestamp>/.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# The claude_chat backend reads this at import time. The CLI runs in an empty
# temp dir, so "project" keeps the user's CLAUDE.md, plugins and installed
# skills (including these very skills) out of the model under test. Forced, not
# defaulted: an inherited "user,project" would silently undo the isolation.
os.environ["CLAUDE_SETTING_SOURCES"] = "project"

import yaml  # noqa: E402
import skillopt  # noqa: E402
from skillopt.datasets.base import BatchSpec, SplitDataLoader  # noqa: E402
from skillopt.envs.base import EnvAdapter  # noqa: E402
from skillopt.model import chat_optimizer, chat_target  # noqa: E402

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent / "skills"

JUDGE_SYSTEM = """You grade an answer against a checklist of assertions.
Judge only from the answer text. Be strict on substance: an assertion passes
only if the answer clearly does what it says; vague or merely implied coverage
fails. Be lenient on wording: the same idea in other words passes, and
examples in an assertion ("e.g. ...") are illustrations, not requirements.
Reply with JSON only, one entry per assertion in the given order:
{"results": [{"pass": true, "reason": "<one short sentence>"}]}"""


def judge(item: dict, answer: str) -> tuple[list[bool], list[str]]:
    checklist = "\n".join(f"{i}. {a}" for i, a in enumerate(item["assertions"], 1))
    user = (
        f"User request:\n{item['question']}\n\n"
        f"What a good answer does:\n{item['reference_text']}\n\n"
        f"Assertions:\n{checklist}\n\n"
        f"Answer to grade:\n{answer}"
    )
    for _ in range(2):
        text, _usage = chat_optimizer(system=JUDGE_SYSTEM, user=user, stage="judge")
        match = re.search(r"\{.*\}", text or "", re.S)
        try:
            results = json.loads(match.group(0))["results"]
        except (AttributeError, ValueError, KeyError, TypeError):
            continue
        if (
            isinstance(results, list)
            and len(results) == len(item["assertions"])
            and all(isinstance(r, dict) and isinstance(r.get("pass"), bool) for r in results)
        ):
            return [r["pass"] for r in results], [str(r.get("reason", "")) for r in results]
    raise RuntimeError(f"judge gave no usable verdict for {item['id']}")


def rollout_one(item: dict, skill: str, pred_dir: Path, max_tokens: int) -> dict:
    answer, _usage = chat_target(system=skill, user=item["question"], max_completion_tokens=max_tokens)
    passed, reasons = judge(item, answer)
    missed = [f"{a} ({r})" for a, ok, r in zip(item["assertions"], passed, reasons) if not ok]

    # EnvAdapter.reflect() reads this path; without it the result teaches nothing.
    task_dir = pred_dir / item["id"]
    task_dir.mkdir(parents=True, exist_ok=True)
    conversation = [
        {"role": "system", "content": skill},
        {"role": "user", "content": item["question"]},
        {"role": "assistant", "content": answer},
    ]
    (task_dir / "conversation.json").write_text(json.dumps(conversation, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "id": item["id"],
        "hard": int(not missed),
        "soft": sum(passed) / len(passed),
        "predicted_answer": answer,
        "question": item["question"],
        "task_description": item["question"],
        "reference_text": item["reference_text"],
        "task_type": item["task_type"],
        "fail_reason": "Missed assertions: " + "; ".join(missed) if missed else "",
        "target_system_prompt": skill,
        "target_user_prompt": item["question"],
        "n_turns": 1,
    }


class AlchemyLoader(SplitDataLoader):
    def load_raw_items(self, data_path: str) -> list[dict]:
        data = json.loads(Path(data_path).read_text(encoding="utf-8"))
        return [
            {
                "id": f"{data['skill_name']}-{e['id']}",
                "question": e["prompt"],
                "reference_text": e.get("expected_output", ""),
                "assertions": e["assertions"],
                "task_type": data["skill_name"],
            }
            for e in data["evals"]
        ]


class AlchemyAdapter(EnvAdapter):
    def __init__(
        self,
        data_path: str = "",
        split_dir: str = "",
        split_mode: str = "ratio",
        split_ratio: str = "3:1:1",
        split_seed: int = 42,
        split_output_dir: str = "",
        workers: int = 4,
        analyst_workers: int = 4,
        failure_only: bool = False,
        minibatch_size: int = 6,
        edit_budget: int = 3,
        seed: int = 42,
        limit: int = 0,
        max_completion_tokens: int = 4096,
    ) -> None:
        self.workers = workers
        self.analyst_workers = analyst_workers
        self.failure_only = failure_only
        self.minibatch_size = minibatch_size
        self.edit_budget = edit_budget
        self.max_completion_tokens = int(max_completion_tokens)
        self.dataloader = AlchemyLoader(
            split_dir=split_dir,
            data_path=data_path,
            split_mode=split_mode,
            split_ratio=split_ratio,
            split_seed=split_seed,
            split_output_dir=split_output_dir,
            seed=seed,
            limit=limit,
        )

    def setup(self, cfg: dict) -> None:
        super().setup(cfg)
        self.dataloader.setup(cfg)

    def get_dataloader(self):
        return self.dataloader

    def build_env_from_batch(self, batch: BatchSpec, **kwargs):
        return list(batch.payload or [])

    def build_train_env(self, batch_size: int, seed: int, **kwargs):
        return self.build_env_from_batch(self.dataloader.build_train_batch(batch_size=batch_size, seed=seed, **kwargs))

    def build_eval_env(self, env_num: int, split: str, seed: int, **kwargs):
        return self.build_env_from_batch(self.dataloader.build_eval_batch(env_num=env_num, split=split, seed=seed, **kwargs))

    def rollout(self, env_manager, skill_content: str, out_dir: str, **kwargs) -> list[dict]:
        pred_dir = Path(out_dir, "predictions")
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            results = list(pool.map(lambda it: rollout_one(it, skill_content, pred_dir, self.max_completion_tokens), env_manager))
        Path(out_dir, "rollouts.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        return results

    def get_task_types(self) -> list[str]:
        return sorted({it["task_type"] for it in self.dataloader.train_items + self.dataloader.val_items + self.dataloader.test_items})


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    if not (SKILLS / name / "evals" / "evals.json").is_file():
        sys.exit("usage: train.py <skill-name> [--eval] [skillopt options]")
    # --eval scores the current SKILL.md on all evals without training.
    evaluate = "--eval" in sys.argv[2:]
    extra = [a for a in sys.argv[2:] if a != "--eval"]

    # A fresh directory per run: SkillOpt resumes from whatever it finds in
    # out_root, so reusing one would silently skip training after a change.
    # Pass --out_root <existing run dir> to resume on purpose.
    out_root = HERE / "runs" / (f"{name}-baseline" if evaluate else name) / time.strftime("%Y%m%d-%H%M%S")
    out_root.mkdir(parents=True, exist_ok=True)
    # _base_ must point into the SkillOpt checkout, which lives outside this repo.
    cfg = yaml.safe_load((HERE / "config.yaml").read_text(encoding="utf-8"))
    cfg["_base_"] = str(Path(skillopt.__file__).resolve().parent.parent / "configs" / "_base_" / "default.yaml")
    cfg_path = out_root / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg, sort_keys=False), encoding="utf-8")

    # SkillOpt's skillopt-eval / skillopt-train entry points
    if evaluate:
        from scripts import eval_only as entry
        skill_args = ["--skill", str(SKILLS / name / "SKILL.md"), "--split", "all"]
    else:
        from scripts import train as entry
        skill_args = ["--skill_init", str(SKILLS / name / "SKILL.md")]

    entry._register_builtins()
    entry._ENV_REGISTRY["alchemy"] = AlchemyAdapter
    sys.argv = [
        "skillopt",
        "--config", str(cfg_path),
        *skill_args,
        "--data_path", str(SKILLS / name / "evals" / "evals.json"),
        "--out_root", str(out_root),
        *extra,
    ]
    entry.main()


if __name__ == "__main__":
    main()
