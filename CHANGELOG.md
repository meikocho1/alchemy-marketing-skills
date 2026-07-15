# Changelog

All notable changes to this project are documented in this file.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning](https://semver.org/).

## [1.2.0] - 2026-07-15

日本語・中国語トリガー追加、著名理論との相互チェック＆リサーチ指示、存在しない外部スキル参照の明示、README のリンク修正と 7 スキル対応。

### Added
- Japanese and Chinese trigger phrases in every skill description (all 7 skills), so 日本語 / 中文 prompts fire the skills as reliably as English ones.
- **Cross-check against the canon** section in every skill: recommendations are sanity-checked against established theory — Kahneman (System 1/2, peak-end, WYSIATI), Kahneman & Tversky (prospect theory), Cialdini (*Influence*, contrast), Ariely, Byron Sharp (*How Brands Grow*, the evidence-based counterweight), Thaler (mental accounting), Thaler & Sunstein (*Nudge*), Ries & Trout (*Positioning*), Zahavi (handicap principle), Spence (signalling theory), Veblen, Aronson (pratfall effect and its competence caveat), Samuelson (revealed preference), Schwartz (*The Paradox of Choice*), Taleb (barbell), Maister (waiting lines), Don Norman, Hofstede + Hall + Erin Meyer (cultural dimensions, with the ecological-fallacy caveat), Steve Blank — with an instruction to name and justify any contradiction instead of silently averaging.
- Research instruction: when a claim is load-bearing or the user asks for evidence or fresh examples, the skill web-searches the named theory/case and cites the source instead of relying on memory.
- README: `cultural-context` and `market-recon` added to the skills tables (EN/JA) — they shipped in 1.1.0 but the README was never updated.
- This changelog, linked from the README.

### Changed
- References to external skills (`marketing-psychology`, `ab-testing`) are now marked "separate plugin — only if installed", so Claude doesn't try to invoke skills this plugin doesn't ship.
- `psycho-logic` description trimmed (routing detail already lives in the body) to stay under the 1024-character description limit after adding the new trigger phrases.

### Fixed
- README: the Goodreads link pointed at the wrong book — ID `42755477` resolves to an unrelated title ("Ben, Mona Lisa"). Now points to Rory Sutherland's *Alchemy* (`55165511`).
- README: the Claude Code docs badge now links to the canonical `https://code.claude.com/docs` (the old `docs.claude.com` URL only worked via redirect).

## [1.1.0]

地域・文化リサーチ層を追加。

### Added
- Region/culture research layer: `cultural-context` (how a market reads a signal — the perception-by-culture lens) and `market-recon` (live, sourced fieldwork on the target market in the local language).

## [1.0.0]

初版リリース。

### Added
- Initial release: `psycho-logic` (router), `reframing`, `costly-signaling`, `counterintuitive-tests`, `experience-design` — each with a bilingual body and eval cases.
