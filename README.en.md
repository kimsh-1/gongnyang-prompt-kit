# 🐾 Gongnyang Prompt Kit VOL.2

**A Claude Code skill that compiles a vague one-liner into a finished gpt-image-2 production prompt.**

<samp>[한국어](README.md) · **English** · [日本語](README.ja.md)</samp>

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) &nbsp;![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757) &nbsp;![target: gpt-image-2](https://img.shields.io/badge/target-gpt--image--2-1E4D40) &nbsp;![library: C1-C12 + P1-P8 + TP1-TP14](https://img.shields.io/badge/library-C1--C12_+_P1--P8_+_TP1--TP14-C19A6B)

![Gongnyang Prompt Kit VOL.2 key visual](docs/main.png)

It takes a request as loose as "make me a poster" and returns a complete production prompt, ready to drop straight into generation. The key visual above was itself generated from a prompt this kit compiled (C11 cinematic key art).

A note on language: the kit's compile records are Korean-first — Korean is the author's working language, and rendering Hangul is one of the harder text tests you can throw at gpt-image-2, so it doubles as a permanent stress test. The grammar the kit teaches (Scene / Camera / Lighting / Color grading / Texture, HEX-pinned palettes, one trailing `AR` token) is language-agnostic and carries over to English prompts one-to-one.

![Compile demo — loose request → complete prompt → validator pass](docs/hero.gif)

Loose request → complete prompt → validator pass. All three steps happen inside the skill. Image generation itself is out of scope — for bulk generation use the `codex-imagegen` skill in [codex-fleet](https://github.com/kimsh-1/codex-fleet); for a single image, feed the prompt straight to `codex`.

> Interactive demo: **[kimsh-1.github.io/gongnyang-prompt-kit](https://kimsh-1.github.io/gongnyang-prompt-kit)**

## What's different — the v3 single routing table

The core of v3 is one routing table. Given a request signal, you pick one row below and read **only** the one reference file that row points to. The canonical routing table lives in exactly one place — [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md) — and the table below is a reader-facing mirror of it.

| When you say | It compiles as | Reference to read |
|---|---|---|
| Solo-figure editorial / fashion spread | C1 · Format B flat-comma | [`editorial-hwabo.md`](skills/image-prompt/references/editorial-hwabo.md) |
| Typography poster · "the type IS the image" | one pattern from TP1–TP14 | [`typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md) → one file in `typo-poster/` |
| Promo graphics · "a properly designed poster" | one pattern from P1–P8 | [`promo-router.md`](skills/image-prompt/references/promo-router.md) → one file in `promo/` |
| Poster · key art · infographic · card-news (SNS info cards) · comic · product atlas · icon · beauty · campaign · mockup | C2–C11 | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md), relevant section |
| Presentation · slide deck | C12 (16:9 default) | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md) §C12 |
| Mood ("make it classy" · "luxury" · "like a film") | look preset L1–L9 drop-in | [`look-presets.md`](skills/image-prompt/references/look-presets.md) |
| Concept fan-out · "start from the concept" | concept axes M1–M10 / R / X / T1–T5 variations | [`concept-axes.md`](skills/image-prompt/references/concept-axes.md) |
| Text placement · fonts · grids · dense text | zone grammar · role labels | [`typography-layout.md`](skills/image-prompt/references/typography-layout.md) |
| Camera · lighting · color vocabulary | result-description vocabulary | [`photo-vocab.md`](skills/image-prompt/references/photo-vocab.md) |
| jsonl batches · model facts · complete examples | jsonl schema · codex skeleton | [`jsonl-and-examples.md`](skills/image-prompt/references/jsonl-and-examples.md) |

Library coverage: categories **C1–C12** · typography posters **TP1–TP14** · promo graphics **P1–P8** · look presets **L1–L9** · concept axes **M1–M10 / R / X / T1–T5**.

## Generation examples — what compiling does to a prompt

Same gpt-image-2 on both sides. **Left is a human's one-liner fed as-is; right is that same one-liner after the kit compiles it** — the only difference is the prompt. The full compile records are in [`examples/showcase.jsonl`](examples/showcase.jsonl). Compiled prompts below are shown verbatim in Korean, exactly as generated — the section labels (Scene / Camera / Lighting / Color grading / Texture / AR) make the structure legible even if you don't read Korean.

#### `make me a badass image` → C11 cinematic key art

| Without the skill | Kit-compiled |
|---|---|
| ![Without the skill — make me a badass image](docs/showcase/SC32B.webp) | ![Kit-compiled — C11 cinematic key art](docs/showcase/SC32.webp) |

<details>
<summary>Full compiled prompt (a giant whale breaching a sea of clouds at dawn)</summary>

```
시네마틱 키아트 — 새벽 구름바다 위로 도약하는 거대 고래.
Scene: 해 뜨기 직전의 구름 바다, 그 위로 거대한 혹등고래 한 마리가 구름 물보라를 흩뿌리며 도약하는 순간, 아래 절벽 끝에 작은 관측자 실루엣 한 명, 상단 하늘 밴드는 비워둔 클린 영역.
Camera: 초광각 vista, 로우 앵글, 인물 대비 압도적 스케일 대비, deep aerial perspective.
Lighting: 지평선의 골드 백라이트가 고래의 림을 태우고, 구름 틈으로 volumetric 광선이 쏟아진다.
Color grading: 새벽 인디고 #1B2440, 골드 #E8B168, 페일 로즈 #E8C4C4.
Texture/Medium: cinematic grain, 옅은 안개 드리프트.
AR 16:9
```

</details>

#### `jazz-bar poster` → C3 Korean poster

| Without the skill | Kit-compiled |
|---|---|
| ![Without the skill — jazz-bar poster](docs/showcase/SC03B.webp) | ![Kit-compiled — C3 Korean poster](docs/showcase/SC03.webp) |

<details>
<summary>Full compiled prompt (note the Text-in-image line — quoted Korean copy with role labels, rendered in-image)</summary>

```
한국어 재즈바 포스터, 상업 인쇄 완성도.
Scene: 상단 1/3 타이틀 밴드, 중앙에 콘트라베이스 연주자의 딥블루 실루엣 일러스트와 담배연기 같은 얇은 곡선, 하단 캡션 밴드. 정돈된 매거진 여백.
Camera: 정면 평면 구성, 중앙 정렬, 풀블리드.
Lighting: 무대 스포트라이트 하나가 실루엣 뒤에서 번지는 글로우.
Color grading: 미드나잇 #101A2E, 크림 #F3EEE2, 브라스 골드 #C9A24B.
Texture/Medium: 매트 아트지, 미세 그레인, 인쇄 톤.
Text-in-image: headline "밤과 재즈" 상단 중앙(굵은 세리프, 크림), caption "매주 금·토" 하단 중앙(콘덴스드 산세리프, 골드).
All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark.
AR 4:5
```

</details>

#### Categories (C1–C10)

| Request → pattern | Without the skill | Kit-compiled |
|---|---|---|
| `fashion spread` → C1 editorial | ![Without the skill](docs/showcase/SC01B.webp) | ![Kit-compiled](docs/showcase/SC01.webp) |
| `lip-balm ad shot` → C2 beauty | ![Without the skill](docs/showcase/SC02B.webp) | ![Kit-compiled](docs/showcase/SC02.webp) |
| `earbud product atlas` → C4 product atlas | ![Without the skill](docs/showcase/SC04B.webp) | ![Kit-compiled](docs/showcase/SC04.webp) |
| `perfume campaign` → C5 campaign | ![Without the skill](docs/showcase/SC05B.webp) | ![Kit-compiled](docs/showcase/SC05.webp) |
| `coffee infographic` → C6 infographic | ![Without the skill](docs/showcase/SC06B.webp) | ![Kit-compiled](docs/showcase/SC06.webp) |
| `savings-tips card-news` → C7 card-news | ![Without the skill](docs/showcase/SC07B.webp) | ![Kit-compiled](docs/showcase/SC07.webp) |
| `granola package` → C8 branding | ![Without the skill](docs/showcase/SC08B.webp) | ![Kit-compiled](docs/showcase/SC08.webp) |
| `rocket 3D icon` → C9 3D icon | ![Without the skill](docs/showcase/SC09B.webp) | ![Kit-compiled](docs/showcase/SC09.webp) |
| `cat 4-panel comic` → C10 comic | ![Without the skill](docs/showcase/SC10B.webp) | ![Kit-compiled](docs/showcase/SC10.webp) |
| `sci-fi key art` → C11 key art | ![Without the skill](docs/showcase/SC11B.webp) | ![Kit-compiled](docs/showcase/SC11.webp) |

#### Look presets (L1–L9)

| Request → look | Without the skill | Kit-compiled |
|---|---|---|
| `luxury watch` → L1 luxury editorial | ![Without the skill](docs/showcase/SC13B.webp) | ![Kit-compiled](docs/showcase/SC13.webp) |
| `dashboard hero` → L5 dark tech | ![Without the skill](docs/showcase/SC17B.webp) | ![Kit-compiled](docs/showcase/SC17.webp) |
| `year-end invitation` → L8 gold foil | ![Without the skill](docs/showcase/SC20B.webp) | ![Kit-compiled](docs/showcase/SC20.webp) |

#### Concept axes (M·T)

| Request → axis | Without the skill | Kit-compiled |
|---|---|---|
| `wave typography poster` → T1 motion translation | ![Without the skill](docs/showcase/SC26B.webp) | ![Kit-compiled](docs/showcase/SC26.webp) |
| `night-market poster, hip and kitsch` → T3 intentional distortion | ![Without the skill](docs/showcase/SC27B.webp) | ![Kit-compiled](docs/showcase/SC27.webp) |
| `whiskey ad poster, make it luxe` → M2 Art Deco | ![Without the skill](docs/showcase/SC28B.webp) | ![Kit-compiled](docs/showcase/SC28.webp) |
| `rock festival poster, make it cool` → M8 Constructivism | ![Without the skill](docs/showcase/SC29B.webp) | ![Kit-compiled](docs/showcase/SC29.webp) |
| `scented-candle brand poster, make it pretty` → M7 Art Nouveau | ![Without the skill](docs/showcase/SC30B.webp) | ![Kit-compiled](docs/showcase/SC30.webp) |
| `electronic party poster, make it hip` → M9 psychedelic | ![Without the skill](docs/showcase/SC31B.webp) | ![Kit-compiled](docs/showcase/SC31.webp) |

## Typography posters (TP1–TP14) — the type IS the image

Fourteen grammars where letterforms are the picture itself: a landscape masked inside the glyphs (TP1), a single word repeated into an infinite tunnel that builds space (TP2), letters stacked into architecture (TP3), shadows and reflections that write the word (TP4), forms carved from real glass, chrome, and balloons (TP7–TP9), segmented paint that snaps into a word from one single viewpoint (TP13), and thousands of micro-letters drawing a portrait (TP14). Pattern definitions are in [`typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md); compile records for every cut are in [`examples/typo-poster.jsonl`](examples/typo-poster.jsonl).

| TP1 · Photo masking (SEOUL) | TP2 · Text tunnel (무한 "infinite") | TP3 · Type architecture (BUILD·WERK) |
|---|---|---|
| ![TP1 photo masking — SEOUL](docs/showcase/TP01.webp) | ![TP2 text tunnel — 무한](docs/showcase/TP02.webp) | ![TP3 type architecture — BUILD WERK](docs/showcase/TP03.webp) |
| **TP4 · Optical phenomenon (쉼 "rest")** | **TP5 · Material destruction (해체 "deconstruct")** | **TP6 · Swiss kinetic (will kern for food)** |
| ![TP4 optical phenomenon — 쉼 shadow](docs/showcase/TP04.webp) | ![TP5 material destruction — 해체](docs/showcase/TP05.webp) | ![TP6 Swiss kinetic — will kern for food](docs/showcase/TP06.webp) |
| **TP7 · Material sculpting (얼음 "ice")** | **TP8 · Liquid chrome (녹아 "melting")** | **TP9 · Inflatable (몰랑 "squishy")** |
| ![TP7 material sculpting — 얼음](docs/showcase/TP07.webp) | ![TP8 liquid chrome — 녹아](docs/showcase/TP08.webp) | ![TP9 inflatable — 몰랑](docs/showcase/TP09.webp) |
| **TP10 · Op-art pattern (진동 "vibration")** | **TP11 · Acid graphics (광란 "frenzy")** | **TP12 · Future medieval (심판 "judgment")** |
| ![TP10 op-art pattern — 진동](docs/showcase/TP10.webp) | ![TP11 acid — 광란](docs/showcase/TP11.webp) | ![TP12 future medieval — 심판](docs/showcase/TP12.webp) |
| **TP13 · Anamorphic illusion (LOOK)** | **TP14 · Micrography (고요 "stillness")** | |
| ![TP13 anamorphic — LOOK](docs/showcase/TP13.webp) | ![TP14 micrography — 고요](docs/showcase/TP14.webp) | |

Korean hero words hold up as-is across most patterns — worth noting because Hangul is a harder glyph-fidelity test than Latin: chrome drip "녹아", balloon "몰랑", op-art "진동", shadow "쉼", all the way to the micro-letter portrait "고요". English hero words (SEOUL, BUILD, LOOK) run through the exact same grammars.

## Promo graphics (P1–P8) — designer poster grammar

A layer that renders in the tone of designer-made promotional material, not the flat SNS card-news look. Eight layout grammars where type is not decoration but physically entangled with the subject, plus a 2–3 color hard-lock and print-finish devices. Orthogonal to the look presets (L) and cross-breedable with them. Pattern definitions are in [`promo-router.md`](skills/image-prompt/references/promo-router.md).

| P1 Type-mask · photo inside the letters | P2 Type-environment · isometric terrain | P3 Oversize crop + occlusion |
|---|---|---|
| ![P1 type-mask — seoul](docs/showcase/PR01.webp) | ![P2 type-environment — RUN isometric](docs/showcase/PR02.webp) | ![P3 occlusion — BREW](docs/showcase/PR03.webp) |
| **P5 Meta UI · selection box** | **P6 Street collage** | **P8 Monochrome staging** |
| ![P5 meta UI — FORME selection box](docs/showcase/PR04.webp) | ![P6 street collage — street pop](docs/showcase/PR05.webp) | ![P8 monochrome staging — silver](docs/showcase/PR06.webp) |
| **Occlusion × shadow narrative · "집" (house)** | **Masking × type-environment · "폭풍" (storm)** | **Light shaft × staging · "고요" (stillness)** |
| ![집 — a 3D glyph's shadow becomes a night skyline](docs/showcase/PR07.webp) | ![폭풍 — storm clouds inside the letters, lightning strikes the can through a gap](docs/showcase/PR08.webp) | ![고요 — an amber light shaft falls through the letters onto whiskey](docs/showcase/PR09.webp) |
| **Masking × selection · "소리" (sound)** | **Rotation axis × masking · "바다" (sea)** | **Letters = bookshelf · "책방" (bookshop)** |
| ![소리 — halftone crowd, one glyph selected in color](docs/showcase/PR10.webp) | ![바다 — vertical masking + 90-degree rotated photo](docs/showcase/PR11.webp) | ![책방 — two glyphs are actual bookshelf furniture](docs/showcase/PR12.webp) |

The bottom six cuts are a cross-breed set — 2–3 patterns bred together and anchored with a Korean headline. For Korean headlines, 2 characters is the safe zone for both masking and extrusion.

## Hongdae indie mood line (L9)

Look preset L9 decomposes the "effortlessly artsy" vibe of Hongdae — Seoul's indie art and music district — into 8 generation engines: word-world typography (A), art-movement reinterpretation (B), collage (C), film photography (D), Riso zine (E), mixed media (F), still life (G), and shadow narrative (H), where an object's cast shadow bleeds into a cinematic scene.

| H · Shadow narrative (film camera) | A · Word-world (dawn) | D · Film (night) |
|---|---|---|
| ![shadow narrative — film camera](docs/showcase/HD01.webp) | ![word-world — dawn](docs/showcase/HD02.webp) | ![film — night](docs/showcase/HD03.webp) |
| **B · Movement (psychedelic)** | **E · Riso zine (poster)** | **C · Collage (Memphis)** |
| ![movement — psychedelic](docs/showcase/HD04.webp) | ![Riso zine — poster](docs/showcase/HD05.webp) | ![collage — Memphis](docs/showcase/HD06.webp) |
| **G · Still life (wabi-sabi)** | **F · Mixed media (face montage)** | **D · Film (pojangmacha street stall)** |
| ![still life — wabi-sabi](docs/showcase/HD07.webp) | ![mixed media — face montage](docs/showcase/HD08.webp) | ![film — pojangmacha](docs/showcase/HD09.webp) |
| **H · Shadow narrative (whiskey glass)** | **A · Word-world (summer night)** | **D · Film (basement club)** |
| ![shadow narrative — whiskey glass](docs/showcase/HD10.webp) | ![word-world — summer night](docs/showcase/HD11.webp) | ![film — basement club](docs/showcase/HD12.webp) |

## Presentation decks & complex diagrams (C6·C12)

Presentation slides and complex conceptual diagrams compile through the same kit — sequence diagrams, many-to-many networks, feedback loops, and high-density slides rendering 400–800 Korean characters each (the density lever works the same for English copy).

| Ultra-dense text (Transformer, ~700 chars) | Cache-strategy 5-way comparison (~700 chars) |
|---|---|
| ![Transformer architecture ultra-dense slide](examples/diagram-gallery/dense-16x9/DN-TRANSFORMER-001.png) | ![Distributed cache strategy 5-way comparison](examples/diagram-gallery/dense-16x9/DN-CACHE-008.png) |
| **TCP sequence diagram (lifelines · crossing messages)** | **21:9 data slide (ticks · value labels)** |
| ![TCP 3-way handshake sequence](examples/diagram-gallery/complex-16x9/CX-TCP-002.png) | ![Quarterly growth report data slide](examples/diagram-gallery/deck-21x9/D12-DATA-007.png) |

The full 40-cut gallery and source prompt jsonl are in [`examples/diagram-gallery/`](examples/diagram-gallery/). Three takeaways — the primary lever for text accuracy is canvas height (700–800 characters stay stable at 16:9 and 2:3), pin only the critical labels in quotes and delegate body density to the free-write zone, and diagrams go through the front door once you specify nodes, links, and direction in concrete sentences.

## Core rules — highlights

These aren't rules for making images come out well; they block the habits that make images come out badly. Full text in [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md), §Iron Rules.

| Rule | Gist |
|---|---|
| **Tiered negatives** | gpt-image-2 renders scene negatives ("no crowd") using that very word. All scene exclusions are rewritten positively (Tier-0) by default. Only two exception lanes — Tier-1 text-render guards (a 7-item whitelist, only when there is rendered text) and Tier-2 editorial-compliance pair (only when explicitly declared; the canonical text lives in one place, `editorial-hwabo.md` §3). The validator catches every negation outside the whitelist. |
| **No SD dead vocabulary** | `masterpiece / 8k / trending on artstation`, weights like `(word:1.3)`, `--ar` flags — and empty adjectives like "pretty, luxurious, award-winning" — are all noise. Reduce them to numbers, bodily responses, and concrete examples. |
| **Size lock** | The codex (`$imagegen`) path is safe with exactly 6 sizes — 1:1 `1024x1024` · 2:3/3:4/4:5 `1024x1536` · 3:2/4:3 `1536x1024` · 16:9 `1792x1024` · 9:16 `1024x1792` · dense/multi-cut `2048x2048`. No `auto`, no leading `[AR ...]` bracket — only a single trailing `AR x:y` token. |
| **Never post-process text onto images** | Text is rendered inside the image via the prompt (quoted copy + role labels + a free-write zone). Compositing text onto a generated PNG in code (PIL, ImageMagick, SVG) never matches the font, kerning, or tone. Text errors are fixed only by editing the prompt and regenerating. |
| **Gear specs → result description** | The model doesn't know `Canon R5 f/1.4`. Write the result: "shallow DoF, background falls off softly". |
| **Pin numbers** | HEX palette (3–5 colors per cut), Kelvin, `key:fill 1:2`. |
| **1 line = 1 cut = 1 call** | Don't grid multiple cuts onto one canvas. Multiple cuts are N lines. |

## Install & usage

```bash
git clone https://github.com/kimsh-1/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

In Claude Code, run it with triggers like "write an image prompt", "editorial spread prompt", "key art", "typography poster", or `/image-prompt`. Installing via symlink means repo updates apply automatically. The validator requires Node.js.

Check compiled prompts with the validator. It is tier-aware and flags only negatives outside the whitelist.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt        # text mode
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                     # regression self-test
```

It returns `{ok, format, tier, errors, warnings}` JSON. Negatives outside the whitelist, leading brackets, SD dead vocabulary, size-lock violations, and residual slot tokens are `error` (with a positive-rewrite hint); empty adjectives, missing HEX, and the like are `warning`. Passing and failing samples are in [`examples/`](examples/).

To go all the way to generation you need a [Codex CLI](https://github.com/openai/codex) login + ChatGPT Plus/Pro.

## v3.0.0 — what changed and how it was verified

v3 is a structural refactor, not a rule expansion. The skill body was compressed and routing was consolidated into one place.

**Refactor, measured**

- SKILL.md body 17.6KB → 9.5KB
- Routing duplicated in 3 places → a single 10-row routing table (canonical copy lives only in SKILL.md)
- Frontmatter description 940 chars → 316 chars
- The Tier-2 frozen wording now has one canonical home: `editorial-hwabo.md` §3
- New release checklist: [`RELEASING.md`](RELEASING.md)

**Verification, measured**

- `check_prompt.mjs` fixtures **16/16 PASS**
- Fresh-context routing quiz **8/8** (an agent reading the skill for the first time reaches the right answer from the routing table alone)
- Rule-loss audit: **0 findings** — every normative v2 rule confirmed preserved

**50-cut live test (2026-07-20)**

Ten agents that had read only the new SKILL.md compiled 50 cuts spanning C1–C12, TP1–TP14, P1–P8, and the look/concept axes.

| Stage | Result |
|---|---|
| Validator pass | 50/50 |
| Real generation via codex (`$imagegen`) | 50/50 succeeded |
| Moderation refusals | 0 |
| Wall time | 13.5 min (auto-scaled, peak 13 workers) |

## Structure

![Kit structure — loose request → skill core → references → complete prompt → validator → image generation](docs/architecture.png)

A loose request passes through the skill core and references to become a complete prompt, and must clear the validator before generation. SKILL.md keeps only the always-loaded core; deep detail is split into `references/` (progressive disclosure).

```
skills/image-prompt/
├─ SKILL.md                      # core — workflow · single routing table · iron rules · Format A/B · size lock · validator
├─ references/                   # deep content, read only when the routing table points to it
│  ├─ category-patterns.md       #   C1–C12 cut types · default AR · comics · key art · decks
│  ├─ look-presets.md            #   look presets L1–L9, drop-in
│  ├─ promo-router.md            #   promo graphics router (P1–P8) · finishing devices · cross-breeds
│  ├─ promo/                     #     P1–P8 per-pattern drop-ins (load only the one the router picks)
│  ├─ typo-poster-router.md      #   typography-poster router (TP1–TP14)
│  ├─ typo-poster/               #     TP1–TP14 per-pattern drop-ins (load only the one the router picks)
│  ├─ concept-axes.md            #   concept axes — movements M1–M10 · bodily-response translation · contradiction pairs · color translation · typographic art T1–T5
│  ├─ typography-layout.md       #   zone grammar · role labels · font vocabulary · grids
│  ├─ editorial-hwabo.md         #   editorial Format B · 12 slots · Tier-2 canonical text (§3)
│  ├─ jsonl-and-examples.md      #   jsonl schema · model facts · codex call skeleton
│  ├─ photo-vocab.md             #   camera · lighting · film · composition · color vocabulary (Korean/English mixed)
│  └─ style-taxonomy.md          #   21 fashion genres + persona DNA
└─ scripts/
   ├─ check_prompt.mjs           # tier-aware validator (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # regression test fixtures
```

## Releasing & license

The 6-step checklist for adding a pattern family or changing a rule is in [`RELEASING.md`](RELEASING.md) — a release requires updating the version, description, routing table, all three READMEs, the installed copy, and the validator together.

Licensed under [MIT](LICENSE).
