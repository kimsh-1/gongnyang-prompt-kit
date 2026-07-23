<div align="center">

<img src="docs/main.png" alt="Gongnyang Prompt Kit VOL.2 key visual" width="720">

# 🐾 Gongnyang Prompt Kit VOL.2

**A Claude Code skill that compiles a vague one-liner into a finished gpt-image-2 prompt.**

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) &nbsp;![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757) &nbsp;![target: gpt-image-2](https://img.shields.io/badge/target-gpt--image--2-1E4D40) &nbsp;![library: C1-C12 + P1-P8 + TP1-TP14](https://img.shields.io/badge/library-C1--C12_+_P1--P8_+_TP1--TP14-C19A6B)

[Demo site](https://gongnyang.github.io/gongnyang-prompt-kit) · [Install](#quickstart) · [Routing](#routing) · [한국어](README.md) · [日本語](README.ja.md)

</div>

<p align="center">
  <img src="docs/hero.gif" alt="Compile demo — loose request → complete prompt → validator pass" width="720">
</p>

<p align="center"><sub>Loose request → complete prompt → validator pass — all three steps happen inside the skill. The key visual above was itself generated from a prompt this kit compiled (C11 cinematic key art).</sub></p>

## Why

- **Naive prompts lose** — feed in a one-liner like "make me a poster" as-is, and the model hands back a result exactly as vague as the request.
- **The compiler approach** — the request signal maps to one row of a routing table, and that single pattern produces a complete Korean production prompt ready to drop straight into generation.
- **Validator gate** — negatives outside the whitelist, deprecated SD vocabulary, and size-lock violations are caught as `error`s before anything reaches generation.
- **Generation is out of scope** — for bulk generation use the `codex-imagegen` skill in [codex-fleet](https://github.com/gongnyang/codex-fleet); for a single image, feed the prompt straight to `codex`.

## The only difference is the prompt

Same gpt-image-2 — **left: a human one-liner (`개쩌는 이미지 하나 만들어줘` — "just make me one badass image") fed in as-is; right: that same one-liner compiled by the kit.**

| Without the skill | Kit-compiled — C11 cinematic key art |
|---|---|
| ![Without the skill — "just make me one badass image"](docs/showcase/SC32B.webp) | ![Kit-compiled — C11 cinematic key art](docs/showcase/SC32.webp) |

<details>
<summary>Full compiled prompt</summary>

The kit compiles into Korean — the author's working language, and rendering Hangul is one of the harder text tests you can throw at gpt-image-2. The Scene / Camera / Lighting / Color grading / Texture grammar carries over to English prompts one-to-one.

```
시네마틱 키아트 — 새벽 구름바다 위로 도약하는 거대 고래.
Scene: 해 뜨기 직전의 구름 바다, 그 위로 거대한 혹등고래 한 마리가 구름 물보라를 흩뿌리며 도약하는 순간, 아래 절벽 끝에 작은 관측자 실루엣 한 명, 상단 하늘 밴드는 비워둔 클린 영역.
Camera: 초광각 vista, 로우 앵글, 인물 대비 압도적 스케일 대비, deep aerial perspective.
Lighting: 지평선의 골드 백라이트가 고래의 림을 태우고, 구름 틈으로 volumetric 광선이 쏟아진다.
Color grading: 새벽 인디고 #1B2440, 골드 #E8B168, 페일 로즈 #E8C4C4.
Texture/Medium: cinematic grain, 옅은 안개 드리프트.
AR 16:9
```

(Gist: cinematic key art — a giant humpback whale breaching a sea of clouds at dawn, tiny observer silhouette on a cliff edge, gold backlight burning the whale's rim, dawn indigo/gold/pale-rose HEX palette, clean sky band reserved at the top.)

</details>

The full compile record is in [`examples/showcase.jsonl`](examples/showcase.jsonl).

## Quickstart

```bash
git clone https://github.com/gongnyang/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

In Claude Code, trigger it with phrases like "write me an image prompt", "editorial prompt", "key art", "typography poster" — or run `/image-prompt`.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt   # check a prompt you wrote
```

It returns `{ok, format, tier, errors, warnings}` as JSON; passing and failing samples live in [`examples/`](examples/).

> [!NOTE]
> Installing via symlink means repo updates apply automatically. Node.js is required to run the validator; to go all the way to generation, you need a [Codex CLI](https://github.com/openai/codex) login plus ChatGPT Plus/Pro.

<details>
<summary>All validator options</summary>

The validator is tier-aware: it only flags negatives outside the whitelist.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt        # text mode
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                     # regression self-test
```

Negatives outside the whitelist, leading brackets, deprecated SD vocabulary, size-lock violations, and leftover slot tokens are `error`s (with positive-rewrite hints); empty adjectives, missing HEX, and the like are `warning`s.

</details>

## Routing

The core of v3 is one routing table — a request signal picks one row, and you read **only** the one reference file that row points to. The canonical routing table lives in exactly one place, the table in [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md); the table below is a reader-facing mirror of it.

| When you say | It compiles as | Reference to read |
|---|---|---|
| Solo-figure editorial / fashion spread | C1 · Format B flat-comma | [`editorial-hwabo.md`](skills/image-prompt/references/editorial-hwabo.md) |
| Typography poster · "the type IS the image" | one pattern from TP1–TP14 | [`typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md) → one file in `typo-poster/` |
| Promo graphics · "a properly designed poster" | one pattern from P1–P8 | [`promo-router.md`](skills/image-prompt/references/promo-router.md) → one file in `promo/` |
| Poster · key art · infographic · card-news (SNS info cards) · comic · atlas · icon · beauty · campaign · mockup | C2–C11 | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md), relevant section |
| Presentation · slide deck | C12 (16:9 default) | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md) §C12 |
| Mood ("make it classy" · "luxury" · "like a film") | look preset L1–L9 drop-in | [`look-presets.md`](skills/image-prompt/references/look-presets.md) |
| Concept fan-out · "start from the concept" | concept axes M1–M10 / R / X / T1–T5 variations | [`concept-axes.md`](skills/image-prompt/references/concept-axes.md) |
| Text placement · fonts · grids · dense text | zone grammar · role labels | [`typography-layout.md`](skills/image-prompt/references/typography-layout.md) |
| Camera · lighting · color vocabulary | result-description vocabulary | [`photo-vocab.md`](skills/image-prompt/references/photo-vocab.md) |
| jsonl batches · model facts · complete examples | jsonl schema · codex skeleton | [`jsonl-and-examples.md`](skills/image-prompt/references/jsonl-and-examples.md) |

Library coverage: categories **C1–C12** · typography posters **TP1–TP14** · promo graphics **P1–P8** · look presets **L1–L9** · concept axes **M1–M10 / R / X / T1–T5**.

## Core rules

These are not rules for making images come out well — they are rules that block the habits that make images come out badly. The full text is in [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md) §Iron Rules.

| Rule | Gist |
|---|---|
| **Tiered negatives** | gpt-image-2 tends to render scene negatives ("no crowd") as the very thing you excluded. Scene exclusion defaults to positive restatement (Tier-0), always. Only two exception lanes exist — Tier-1 text-render guards (a 7-item whitelist, only when there is rendered text) and Tier-2 editorial compliance pairs (only when explicitly declared; the single source of truth is `editorial-hwabo.md` §3). Any negation outside the whitelist gets caught by the validator. |
| **No deprecated SD vocabulary** | `masterpiece / 8k / trending on artstation`, weight syntax `(word:1.3)`, `--ar` flags — and empty adjectives like "pretty, premium, award-worthy" — are all noise. Reduce them to numbers, bodily reactions, and concrete examples. |
| **Size lock** | The codex (`$imagegen`) path is safe with exactly 6 sizes — 1:1 `1024x1024` · 2:3/3:4/4:5 `1024x1536` · 3:2/4:3 `1536x1024` · 16:9 `1792x1024` · 9:16 `1024x1792` · dense/multi-cut `2048x2048`. No `auto`, no leading `[AR ...]` bracket — exactly one trailing `AR x:y` token. |
| **Never post-process text onto images** | Text is rendered inside the image by the prompt (quoted copy + role labels + a free-writing zone). Compositing text onto the generated PNG in code (PIL, ImageMagick, SVG) always looks off in font, kerning, and tone. Text errors are fixed only by editing the prompt and regenerating. |
| **Gear specs → result descriptions** | The model doesn't know `Canon R5 f/1.4`. Write the result instead: "shallow DoF, background falls off softly". |
| **Pin the numbers** | HEX palette (3–5 colors per cut), Kelvin, `key:fill 1:2`. |
| **1 line = 1 cut = 1 call** | Never draw multiple cuts as a grid on one canvas. Multiple cuts go on N lines. |

## Best cuts

| TP8 · Liquid chrome (녹아 "melt") | TP13 · Anamorphic illusion (LOOK) | TP14 · Micrography (고요 "stillness") |
|---|---|---|
| ![TP8 liquid chrome — 녹아 "melt"](docs/showcase/TP08.webp) | ![TP13 anamorphic illusion — LOOK](docs/showcase/TP13.webp) | ![TP14 micrography — 고요 "stillness"](docs/showcase/TP14.webp) |
| **Occlusion × shadow narrative (집 "home")** | **Masking × typo-environment (폭풍 "storm")** | **L9 shadow narrative (film camera)** |
| ![Occlusion × shadow narrative — 집 "home"](docs/showcase/PR07.webp) | ![Masking × typo-environment — 폭풍 "storm"](docs/showcase/PR08.webp) | ![L9 shadow narrative — film camera](docs/showcase/HD01.webp) |

Full gallery (21 before/after pairs · 14 TP patterns · 12 P cuts · 12 L9 cuts) → [demo site](https://gongnyang.github.io/gongnyang-prompt-kit) · representative dense-diagram cuts live in [`examples/diagram-gallery/`](examples/diagram-gallery/)

## Structure, releases & license

SKILL.md holds only the always-loaded core; deep detail is split into `references/` (progressive disclosure).

<details>
<summary>Full <code>skills/image-prompt/</code> tree</summary>

```
skills/image-prompt/
├─ SKILL.md                      # core — workflow · single routing table · iron rules · Format A/B · size lock · validator
├─ references/                   # deep content, read only when the routing table points to it
│  ├─ category-patterns.md       #   C1–C12 cut types · default ARs · comics · key art · decks
│  ├─ look-presets.md            #   look presets L1–L9, drop-in
│  ├─ promo-router.md            #   promo-graphics router (P1–P8) · finishing devices · crossbreeds
│  ├─ promo/                     #     P1–P8 per-pattern drop-ins (load only the 1 the router picks)
│  ├─ typo-poster-router.md      #   typography-poster router (TP1–TP14)
│  ├─ typo-poster/               #     TP1–TP14 per-pattern drop-ins (load only the 1 the router picks)
│  ├─ concept-axes.md            #   concept axes — movements M1–M10 · bodily-reaction translation · contradiction pairs · color translation · typo art T1–T5
│  ├─ typography-layout.md       #   zone grammar · role labels · font vocabulary · grids
│  ├─ editorial-hwabo.md         #   editorial Format B · 12 slots · Tier-2 canon (§3)
│  ├─ jsonl-and-examples.md      #   jsonl schema · model facts · codex call skeleton
│  ├─ photo-vocab.md             #   camera · lighting · film · composition · color vocabulary + Korean/English mixing
│  └─ style-taxonomy.md          #   21 fashion styles + persona DNA
└─ scripts/
   ├─ check_prompt.mjs           # tier-aware validator (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # regression-test fixtures
```

</details>

Change history & verification measurements → [GitHub Releases](https://github.com/gongnyang/gongnyang-prompt-kit/releases) · release checklist [`RELEASING.md`](RELEASING.md) · license [MIT](LICENSE)

---

<div align="center">
<sub>🐾 vague one-liner → finished prompt — <a href="https://gongnyang.github.io/gongnyang-prompt-kit">gongnyang.github.io/gongnyang-prompt-kit</a></sub>
</div>
