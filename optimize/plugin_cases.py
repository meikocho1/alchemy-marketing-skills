"""Turn skills/<name>/evals/evals.json into cases for `claude plugin eval`.

    python3 optimize/plugin_cases.py                # every skill except market-recon
    python3 optimize/plugin_cases.py market-recon   # only the named skills
    claude plugin eval . --eval-dir optimize/cases --model sonnet --no-publish

train.py scores one SKILL.md forced in as the system prompt. These cases score
the plugin as installed: Claude sees every skill description and decides for
itself whether to load one, and each case also runs with no plugin, so the
report shows what the skills add (the Δ column). Two unscored graders per case
report triggering: `fired` (this case's skill was loaded) and `fired_any` (any
skill of this plugin was). Cases are tagged with the skill name and the prompt
language (en / ja / zh) for --tag.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent / "skills"
CASES = HERE / "cases"
# These skills need web search, which a run only gets when you pass
# `--allow-tools WebSearch WebFetch`, so their cases are generated only when named.
NEEDS_WEB = {"market-recon"}
WEB_MAX_TURNS = 40  # a recon answer takes many searches; the default of 10 cuts it off


def language(text: str) -> str:
    if re.search(r"[぀-ヿ]", text):  # kana
        return "ja"
    return "zh" if re.search(r"[一-鿿]", text) else "en"


def fired(skills: str) -> dict:
    # Matches both "reframing" and "alchemy-marketing:reframing".
    return {"type": "tool_used", "tool": "Skill", "input_match": rf'"skill"\s*:\s*"(?:[\w-]+:)?(?:{skills})"'}


def main() -> None:
    every = sorted(p.parent.parent.name for p in SKILLS.glob("*/evals/evals.json"))
    names = sys.argv[1:] or [n for n in every if n not in NEEDS_WEB]
    if unknown := set(names) - set(every):
        sys.exit(f"unknown skill(s): {', '.join(sorted(unknown))}; choose from {', '.join(every)}")
    # Clear every skill's cases, not only the ones regenerated, so a skill left
    # out of this run cannot linger from an earlier one. results/ is kept.
    for stale in every:
        shutil.rmtree(CASES / stale, ignore_errors=True)
    for name in names:
        execution, judge = {"allowed_tools": ["Skill"]}, {}
        if name in NEEDS_WEB:
            execution = {"allowed_tools": ["Skill", "WebSearch", "WebFetch"], "max_turns": WEB_MAX_TURNS}
            # Assertions like "searches local-language sources" are about the
            # searches, which the final answer alone does not show.
            judge = {"focus": "trace"}
        evals = json.loads((SKILLS / name / "evals" / "evals.json").read_text(encoding="utf-8"))["evals"]
        for e in evals:
            case = {
                "schema_version": "1.1",
                "name": f"{name}-{e['id']}",
                "tags": [name, language(e["prompt"])],
                "expected_outcome": e.get("expected_output", ""),
                "execution": {"prompt": e["prompt"], **execution},
                "graders": [
                    *({"name": f"a{i}", "type": "llm", "criteria": a, **judge} for i, a in enumerate(e["assertions"], 1)),
                    {"name": "fired", **fired(name)},
                    {"name": "fired_any", **fired("|".join(every))},
                ],
            }
            path = CASES / name / str(e["id"]) / "case.yaml"
            path.parent.mkdir(parents=True)
            # JSON is valid YAML, so no YAML library is needed.
            path.write_text(json.dumps(case, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{name}: {len(evals)} cases")


if __name__ == "__main__":
    main()
