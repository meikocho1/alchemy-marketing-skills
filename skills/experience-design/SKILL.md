---
name: experience-design
description: "Fix the psychologically significant moment, not the logically significant metric — Rory Sutherland on experience. Use when the outcome is fine but the journey feels bad: complaints about waiting, anxiety, uncertainty, or 'it's technically fast/cheap/correct but people still hate it'; when the user asks 'how do we reduce complaints', 'how do we make waiting/onboarding/checkout feel better', 'people are anxious during X', or is about to spend big to shave a number (wait time, load time, steps) when the real pain is how the moment feels. Covers uncertainty reduction, idle vs occupied waiting, and the peak-end rule. Inspired by Rory Sutherland's *Alchemy*. Routed to from psycho-logic."
metadata:
  version: 1.1.0
---

# Experience Design — fix the felt moment, not the metric

Engineers optimise the average and the total. Humans remember the peaks, the end, and how uncertain they felt. The cheap, high-leverage fix is almost always in the *feeling* of a moment, not in the metric that describes it.

## The principle

The number ("8 minute wait," "3 second load," "5 form fields") is not the experience. Attack the experience directly:

- **Uncertainty hurts more than delay.** Not knowing how long is worse than waiting a known amount. A progress bar, an ETA, or a visible queue position can beat an actual speed-up — at a fraction of the cost.
- **Occupied time feels shorter than idle time.** People aren't angry about *waiting*; they're angry about *waiting with nothing happening*. Give the wait a purpose or a view and the same duration feels fine.
- **People judge an experience by its peak and its end (peak-end rule),** not its average. One great moment and a strong finish outweigh a mediocre middle. Engineer a peak; never let it end on a low.

## Canonical examples (steal these patterns)

- **The Uber map.** Showing the car moving toward you on a map didn't make it arrive faster — it killed the *uncertainty*. The anxiety, not the wait, was the problem. (Same insight: arrivals/departures boards, "your food is being prepared," package tracking.)
- **The airport baggage walk.** An airport got complaints about waiting at the carousel. Instead of speeding up the bags, they routed arriving passengers on a longer walk to the carousel — so the bags were already there when people arrived. Total time up, complaints down: idle waiting became occupied walking.
- **Progress bars and "almost there."** Showing progress (even slightly padded) makes the same wait tolerable, because it removes uncertainty and occupies attention.

## How to apply

1. **Map the journey as emotions, not steps.** Walk it as the customer and mark where they feel anxious, ignored, uncertain, or bored — not where the process is technically slow.
2. **Attack uncertainty first (cheapest win).** Wherever someone is waiting blind, add visibility: an ETA, a status, a progress indicator, a "we've got it" acknowledgement. This usually beats making the thing actually faster.
3. **Occupy idle time.** Turn dead waiting into something with a view, a purpose, or a small useful action.
4. **Engineer the peak and the end.** Add one genuinely good moment, and make sure the experience finishes well (a thank-you, a confirmation, a small delight) — that's what gets remembered and retold.
5. **Compare against the metric-fix.** Always show the user the trade: "Reducing the actual wait costs $X and weeks. Removing the uncertainty costs a status indicator. Try the feeling first."

## 日本語の使用例

- 「待ち時間のクレームが多い、人を増やすしかない？」→ 増員（高い解）の前に**不確実性の除去**。"あと何分""今どの工程か"を見せるだけで、実時間を変えずに満足度が上がる（Uberの地図と同じ）。
- 「手続きが多くて離脱する」→ 工程数そのものより、**進捗の可視化と "受け付けました" の即時応答**。プログレスバーと節目の安心メッセージで体感が変わる。
- 「サービス自体は良いのに記憶に残らない」→ **ピーク・エンドの法則**。途中の平均を上げるより、ひとつ強い感動の山と、良い締め（お礼・確認）を設計する。
- 葬儀/シニア領域：「電話がつながるまで不安にさせている」→ 総待ち時間ではなく**"必ず人が出る/折り返す時刻を伝える"** で不確実性を消す。式当日も "次は何をするか" を都度伝えるだけで不安が大きく減る。

## Adapt to the region

Which moment feels anxious, and how much reassurance soothes it, is culturally set. High uncertainty-avoidance markets want more explicit status, ETAs, and confirmation at each step; others find the same hand-holding patronising. What reads as a respectful, delightful peak in one culture can read as excessive or even taboo in another (especially around death, health, and money). Map the journey's *felt* moments with the local reading from **cultural-context**, and mine real local complaints via **market-recon**. 日本語：どの瞬間が不安か、どれだけの安心が要るかは文化で変わる。現地の読み方（cultural-context）と実際の不満（market-recon）で体感の設計を合わせる。

## Related skills

- **cultural-context / market-recon** — localise which moments feel bad and how much reassurance fits
- **psycho-logic** — the router; confirm the problem is the journey, not the outcome
- **counterintuitive-tests** — most experience fixes (e.g. the longer baggage walk) are counterintuitive; test them on behaviour
- **reframing** — sometimes the felt moment is fixed by changing its meaning, not its design
- **marketing-psychology** — peak-end rule, goal-gradient, Zeigarnik, friction in detail
