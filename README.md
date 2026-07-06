# ⚗️ Alchemy Marketing Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skills-d97757.svg)](https://docs.claude.com/en/docs/claude-code)

> **Rory Sutherland's _psycho-logic_ as Claude skills — solve the human perception, not just the engineering or economic metric.**
>
> **Rory Sutherland の「サイコロジック」を Claude スキル化 — エンジニアリングや経済の指標ではなく、人間の「知覚」を解く。**

**[English](#english) · [日本語](#日本語)**

---

## English

The logical fix is usually expensive, slow, and already done by every competitor. The psychological fix is usually cheap, fast, and unexploited. These skills make Claude attack marketing and product problems the way Rory Sutherland does in [_Alchemy_](https://www.goodreads.com/book/show/42755477-alchemy): reframe the meaning, send a costly signal, invert the obvious and test it, or redesign the felt moment.

### The skills

| Skill | What it does |
|---|---|
| **psycho-logic** | The **router**. Diagnoses a problem in human terms, resists the engineer's reflex to fix the metric, and dispatches to one of the four moves below. **Start here.** |
| **cultural-context** | _Research layer (the lens)._ Perception is culturally coded, so the same move can mean the opposite elsewhere. Establishes how a specific region/country/subculture reads a signal — via cultural dials (uncertainty avoidance, high/low context, trust locus, taboo…) — before you reframe or signal. |
| **market-recon** | _Research layer (the fieldwork)._ Goes and looks at the actual target market **now** via local-language web research — local players, price bands, trust signals, taboos, native terms — and synthesises a sourced perception profile the moves consume, instead of reasoning from a stereotype. |
| **reframing** | Change what something _means_ before changing what it _is_ — the cheapest lever. Renaming, recategorising, price / mental-accounting reframes, manufactured value. |
| **costly-signaling** | Why expensive, wasteful, effortful, or self-deprecating actions build trust and desire. Guarantees, brand spend, price-as-quality, and the Pratfall Effect (the honest flaw). |
| **counterintuitive-tests** | "The opposite of a good idea can be a good idea." Generate ideas that don't sound logical, then validate them with cheap, reversible behavioural experiments — because people don't do what they say. |
| **experience-design** | Fix the psychologically significant moment, not the logically significant metric. Uncertainty beats delay, occupied time beats idle time, peak-end beats average. |

Each skill's body is in English; every skill ends with a **日本語の使用例** (Japanese usage examples) section.

### Install

**As a plugin (recommended)**

```
/plugin marketplace add meikocho1/alchemy-marketing-skills
/plugin install alchemy-marketing@alchemy-marketing-skills
```

**Manually** — copy any folder under `skills/` into your `~/.claude/skills/` (or a project's `.claude/skills/`). Each skill is a self-contained `SKILL.md`.

### How it works

Claude loads a skill automatically when your request matches its `description`. Ask a normal marketing question — _"the product's fine but nobody converts,"_ _"how do we make this feel premium without dropping the price,"_ _"why don't people trust us,"_ _"the wait-time complaints are killing us"_ — and the relevant skill fires. **psycho-logic** is the entry point and routes to the others. When the problem touches a new **region or country** — _"will this work in Japan/Germany,"_ _"research this market before we localise"_ — it runs the research layer first (**cultural-context** for the lens, **market-recon** for live local data) so every move fires on that market's reality, not a generic one.

### Credit & disclaimer

The ideas, frameworks, and examples are drawn from the work of **Rory Sutherland** (Vice Chairman, Ogilvy UK) — chiefly his book _Alchemy: The Dark Art and Curious Science of Creating Magic in Brands, Business, and Life_, his TED talks, and his columns. This is an **unofficial, educational** project and is **not affiliated with or endorsed by** Rory Sutherland or Ogilvy. Read the book — it's better than any skill file.

Psycho-logic is for making real things better and surfacing real value. Signals should be honest, scarcity real, and reframes truthful. A trick that doesn't survive the customer finding out is a liability, not a tactic.

---

## 日本語

論理的な打ち手はたいてい高くて遅く、競合も全員すでにやっています。心理的な打ち手はたいてい安くて速く、まだ誰も使っていません。これらのスキルは、Rory Sutherland が著書 [_Alchemy_](https://www.goodreads.com/book/show/42755477-alchemy) で示した流儀で Claude にマーケティング/プロダクトの問題を解かせます — **意味を変える・コストのかかるシグナルを送る・当たり前の逆を試す・体感する瞬間を作り直す**。

### スキル一覧

| スキル | 役割 |
|---|---|
| **psycho-logic** | **ルーター**。問題を人間の言葉で言い換え、「指標を直す」というエンジニアの反射を抑え、下の4つの打ち手へ振り分ける。**まずここから。** |
| **cultural-context** | _リサーチ層（レンズ）_。知覚は文化で決まるので、同じ打ち手が別の市場では逆の意味になり得る。文化ダイヤル（不確実性回避・高/低コンテクスト・信頼の所在・タブー等）で、その地域/国/サブカルチャーが**シグナルをどう読むか**を先に確立する。 |
| **market-recon** | _リサーチ層（現地調査）_。一般論やステレオタイプで推測せず、**現地語のWeb調査で対象市場を今すぐ観察**する — 現地プレイヤー・価格帯・信頼シグナル・タブー・現地語彙 — し、各手法が使える"知覚プロファイル"に落とす。 |
| **reframing** | 中身（_what it is_）より先に「意味」（_what it means_）を変える、最も安いレバー。改名・再カテゴリ化・価格やメンタルアカウンティングの言い換え・価値の演出。 |
| **costly-signaling** | なぜ高価・無駄・手間・自虐が信頼と欲求を生むのか。保証、ブランド広告費、価格＝品質シグナル、プラットフォール効果（正直な弱点）。 |
| **counterintuitive-tests** | 「良いアイデアの逆もまた良いアイデアになりうる」。論理的に聞こえないアイデアを生成し、安く・元に戻せる行動実験で検証する — 人は言う通りには動かないから。 |
| **experience-design** | 論理的に重要な「指標」ではなく、心理的に重要な「瞬間」を直す。不確実性＞遅延、手持ち無沙汰＞占有時間、平均＜ピーク・エンド。 |

各スキルの本文は英語ですが、すべてのスキルの末尾に **日本語の使用例** セクションがあります（葬儀/シニア文脈の例を含む）。

### インストール

**プラグインとして（推奨）**

```
/plugin marketplace add meikocho1/alchemy-marketing-skills
/plugin install alchemy-marketing@alchemy-marketing-skills
```

**手動** — `skills/` 配下の任意のフォルダを `~/.claude/skills/`（またはプロジェクトの `.claude/skills/`）にコピーするだけ。各スキルは単独で完結した `SKILL.md` です。

### 仕組み

リクエストがスキルの `description` に一致すると、Claude が自動でそのスキルを読み込みます。普通のマーケティングの相談 — _「商品は良いのに全然売れない」_、_「値下げせずに高級感を出したい」_、_「なぜ信頼されないのか」_、_「待ち時間のクレームがひどい」_ — を投げれば該当スキルが発火します。**psycho-logic** が入口になり、他へ振り分けます。**地域や国**が関わる相談 — _「これは日本/ドイツで通用する？」_、_「展開前に市場を調べて」_ — では、まずリサーチ層（**cultural-context** でレンズ、**market-recon** で現地の生データ）を回し、各手法が一般論ではなく**その市場の実態**の上で発火するようにします。

### クレジットと免責

アイデア・フレームワーク・事例は **Rory Sutherland**（Ogilvy UK 副会長）の仕事 — とりわけ著書 _Alchemy: The Dark Art and Curious Science of Creating Magic in Brands, Business, and Life_、TED トーク、コラム — に基づいています。本プロジェクトは **非公式・教育目的** であり、Rory Sutherland 氏および Ogilvy とは **一切関係なく、公認されたものでもありません**。原著をぜひ読んでください — どんなスキルファイルよりも面白いです。

サイコロジックは、実体を本当に良くし、本物の価値を引き出すためのものです。シグナルは正直に、希少性は本物で、リフレーミングは真実であるべき。顧客に知られたら崩れるトリックは、戦術ではなく負債です。

---

## License / ライセンス

[MIT](./LICENSE) © 2026 meiko.cho
