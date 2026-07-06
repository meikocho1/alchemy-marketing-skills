---
name: counterintuitive-tests
description: "Generate ideas that don't sound logical, then validate them with cheap behavioural experiments — Rory Sutherland's 'the opposite of a good idea can be a good idea' plus revealed-preference testing. Use when the obvious/logical solution is saturated and the user wants genuinely different options, asks 'what's a creative/unconventional angle', 'how do we stand out', 'should we run a test/experiment', 'how do we know what people actually want', or is about to trust a survey/focus group. Covers deliberate inversion of the obvious move, why stated preferences lie, and designing small reversible experiments that watch behaviour. Inspired by Rory Sutherland's *Alchemy*. Routed to from psycho-logic."
metadata:
  version: 1.1.0
---

# Counterintuitive Tests — invert the obvious, then watch behaviour

Two moves: (1) deliberately generate the ideas that sound *wrong*, because the sensible ideas are already taken; (2) never trust what people *say* about them — run a cheap, reversible experiment and watch what they *do*.

## Why the obvious idea is the wrong default

Logical optimisation converges: every competent competitor finds the same "best practice," so it stops being an advantage. The remaining opportunities are the moves that don't survive a rational business case — which is exactly why nobody has tried them. "Doesn't make sense" is not a reason to reject an idea; it's a reason it might still be available.

- **Red Bull** launched a small, expensive can of bad-tasting drink. Every logical signal said fail. The "wrongness" *was* the positioning — it must do something.
- **Raising the price** sometimes raises sales (it changes the signal — see costly-signaling).
- **Removing** features/options/steps often beats adding them (paradox of choice).

## Why you must test behaviour, not opinions

> People don't think what they feel, don't say what they think, and don't do what they say.

Surveys and focus groups capture *post-hoc rationalisations*, not causes. Nobody in a focus group asked for Red Bull. Stated preference is cheap talk; **revealed preference** (what they actually clicked, bought, kept) is the only honest data. So your job isn't to *ask* whether the counterintuitive idea works — it's to *expose people to it* and measure behaviour.

## How to apply

1. **Write the obvious solution down.** The thing every competitor would do. This is your "do not just do this" baseline.
2. **Invert it on purpose.** For each obvious move, generate its opposite and ask "under what circumstances would the opposite be *better*?" (Charge more. Offer less. Make it slower but nicer. Hide the price. Add friction. Remove a feature.) Keep the ones that aren't insane on inspection.
3. **Design a cheap, reversible test.** The whole point of a counterintuitive idea is you can't reason your way to the answer — so make the experiment so cheap and reversible that you don't need to. A/B test, a soft launch to one segment, a fake-door, a landing page, one store. Small, fast, undoable.
4. **Measure behaviour, not approval.** Define the behavioural metric *before* running (clicks, purchases, retention, completion). Ignore "would you…?" survey answers about the idea.
5. **Let surprising-but-real results win.** If the illogical version beats the logical one on behaviour, ship it — even if you can't fully explain why. It doesn't have to make sense to work.

## How to think about the experiment

- Bias toward **many small reversible bets** over one big committed one (barbell: safe core, cheap weird experiments).
- A test that can't *fail* (no clear behavioural metric, no control) isn't a test — it's theatre.
- Negative results are wins: a cheap experiment that kills a bad idea saved you the expensive version.

## 日本語の使用例

- 「競合と同じ訴求しか思いつかない」→ まず**当たり前の解**を書き出し、その**逆**を1つずつ生成（"もっと高く" "機能を減らす" "あえて遅く・丁寧に" "価格を最後まで見せない"）。安く・元に戻せる形で検証。
- 「アンケートでは好評だったのに売れない」→ **言うこと≠やること**。アンケート（安い口先）ではなく、ランディングページや少数セグメントへのソフトローンチで**行動（購入・離脱）**を測る。
- 「値上げしたら売れなくなりそう」→ 直感で却下せず、1セグメント・期間限定の**可逆なA/B**で行動を見る。論理ではなく結果に判断させる。
- 葬儀/シニア領域：「分かりやすさ＝情報を増やす、が定石」→ 逆に**選択肢と情報を削る**版を作り、問い合わせ完了率で比較する。

## Adapt to the region

What counts as "the obvious move" is itself local — the saturated best-practice in one market can be the untried inversion in another. And this is where the research layer's *hypotheses* get resolved: cultural dials and recon give you educated guesses about a new market, but a stereotype is still just cheap talk. Turn each into a cheap, reversible behavioural test in that market rather than betting on the assumption. 日本語：市場ごとに"当たり前"が違う。cultural-context / market-recon の仮説は断定せず、その市場での可逆な行動実験で確かめる。

## Related skills

- **cultural-context / market-recon** — supply the market hypotheses this skill validates by behaviour
- **psycho-logic** — the router; use it to decide which obvious move to invert
- **reframing** / **costly-signaling** — common sources of the counterintuitive idea you'll test
- **experience-design** — many counterintuitive wins are journey changes; test them the same way
- **ab-testing** / **marketing-psychology** — mechanics of running tests and the biases involved
