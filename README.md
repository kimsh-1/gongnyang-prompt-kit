<div align="center">

<img src="docs/main.png" alt="공냥 프롬프트 킷 VOL.2 키비주얼" width="720">

# 🐾 공냥 프롬프트 킷 VOL.2

**막연한 한마디를 gpt-image-2 완성 프롬프트로 컴파일하는 Claude Code 스킬.**

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) &nbsp;![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757) &nbsp;![target: gpt-image-2](https://img.shields.io/badge/target-gpt--image--2-1E4D40) &nbsp;![library: C1-C12 + P1-P8 + TP1-TP14](https://img.shields.io/badge/library-C1--C12_+_P1--P8_+_TP1--TP14-C19A6B)

[데모 사이트](https://gongnyang.github.io/gongnyang-prompt-kit) · [설치](#quickstart) · [라우팅](#라우팅) · [English](README.en.md) · [日本語](README.ja.md)

</div>

<p align="center">
  <img src="docs/hero.gif" alt="컴파일 데모 — 거친 요청 → 완성 프롬프트 → 검증기 통과" width="720">
</p>

<p align="center"><sub>거친 요청 → 완성 프롬프트 → 검증기 통과 — 세 단계가 스킬 안에서 끝난다. 위 키비주얼도 이 킷으로 컴파일한 프롬프트(C11 시네마틱 키아트)로 생성했다.</sub></p>

## 왜 필요한가

- **나이브 프롬프트는 진다** — "포스터 하나 만들어줘" 수준의 한 줄을 그대로 넣으면, 모델은 그 막연함 그대로의 결과를 돌려준다.
- **컴파일러 접근** — 요청 신호를 라우팅 표에서 한 행으로 매핑하고, 그 패턴 하나로 바로 생성에 넣을 수 있는 완성 한국어 프로덕션 프롬프트를 만든다.
- **검증기 게이트** — 화이트리스트 밖 네거티브·SD 폐기 어휘·사이즈 락 위반은 생성으로 넘어가기 전에 `error`로 잡힌다.
- **생성은 범위 밖** — 대량 생성은 [codex-fleet](https://github.com/gongnyang/codex-fleet)의 `codex-imagegen` 스킬, 한 장이면 `codex`에 직접 넣는다.

## 차이는 프롬프트뿐

같은 gpt-image-2다 — **왼쪽은 사람이 친 한 줄(`개쩌는 이미지 하나 만들어줘`)을 그대로 넣은 결과, 오른쪽은 그 한 줄을 킷이 컴파일해서 넣은 결과.**

| 스킬 없이 | 킷 컴파일 — C11 시네마틱 키아트 |
|---|---|
| ![스킬 없이 — 개쩌는 이미지 하나 만들어줘](docs/showcase/SC32B.webp) | ![킷 컴파일 — C11 시네마틱 키아트](docs/showcase/SC32.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

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

전체 컴파일 레코드는 [`examples/showcase.jsonl`](examples/showcase.jsonl).

## Quickstart

```bash
git clone https://github.com/gongnyang/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

Claude Code에서 "이미지 프롬프트 써줘" · "화보 프롬프트" · "키아트" · "타이포 포스터" 같은 트리거나 `/image-prompt`로 실행한다.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt   # 작성한 프롬프트 검사
```

`{ok, format, tier, errors, warnings}` JSON을 반환하며, 통과·실패 샘플은 [`examples/`](examples/)에 있다.

> [!NOTE]
> 심볼릭 링크로 설치하면 레포 업데이트가 자동 반영된다. 검증기 실행에는 Node.js, 생성까지 이으려면 [Codex CLI](https://github.com/openai/codex) 로그인 + ChatGPT Plus/Pro가 필요하다.

<details>
<summary>검증기 옵션 전체</summary>

검증기는 티어를 인지해서 화이트리스트 밖 네거티브만 잡는다.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt        # 텍스트 모드
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                     # 회귀 셀프테스트
```

화이트리스트 밖 네거티브·앞 브래킷·SD 폐기 어휘·사이즈 락 위반·슬롯 토큰 잔존은 `error`(긍정형 rewrite 힌트 포함), 빈 형용사·HEX 누락 등은 `warning`.

</details>

## 라우팅

v3의 코어는 라우팅 표 하나다 — 요청 신호로 한 행을 고르고, 그 행이 가리키는 레퍼런스 파일 **하나만** 읽는다. 라우팅 정본은 [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md)의 표 한 곳뿐이며, 아래는 그 독자용 미러다.

| 이렇게 말하면 | 이렇게 컴파일된다 | 읽는 레퍼런스 |
|---|---|---|
| 단독 인물 화보·에디토리얼 | C1 · Format B 플랫 콤마형 | [`editorial-hwabo.md`](skills/image-prompt/references/editorial-hwabo.md) |
| 타이포 포스터·"글자가 곧 이미지" | TP1–TP14 중 패턴 1개 | [`typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md) → `typo-poster/` 1파일 |
| 홍보판촉물·"디자인 잘된 포스터" | P1–P8 중 패턴 1개 | [`promo-router.md`](skills/image-prompt/references/promo-router.md) → `promo/` 1파일 |
| 포스터·키아트·인포그래픽·카드뉴스·만화·도감·아이콘·뷰티·캠페인·목업 | C2–C11 | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md) 해당 절 |
| 프레젠테이션·슬라이드 덱 | C12 (16:9 기본) | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md) §C12 |
| 무드("있어보이게"·"럭셔리"·"영화처럼") | 룩 프리셋 L1–L9 드롭인 | [`look-presets.md`](skills/image-prompt/references/look-presets.md) |
| 시안 다변화·"컨셉부터 잡아줘" | 컨셉 축 M1–M10 / R / X / T1–T5 변주 | [`concept-axes.md`](skills/image-prompt/references/concept-axes.md) |
| 글자 배치·폰트·그리드·밀집 텍스트 | 영역 문법·롤 라벨 | [`typography-layout.md`](skills/image-prompt/references/typography-layout.md) |
| 카메라·조명·색 어휘 | 결과 서술 어휘 | [`photo-vocab.md`](skills/image-prompt/references/photo-vocab.md) |
| jsonl 배치·모델 팩트·완성 예제 | jsonl 스키마·codex 골격 | [`jsonl-and-examples.md`](skills/image-prompt/references/jsonl-and-examples.md) |

라이브러리 커버 범위: 카테고리 **C1–C12** · 타이포 포스터 **TP1–TP14** · 홍보판촉물 **P1–P8** · 룩 프리셋 **L1–L9** · 컨셉 축 **M1–M10 / R / X / T1–T5**.

## 핵심 규칙

잘 나오게 하는 규칙이 아니라 안 나오게 만드는 습관을 막는 규칙이다 — 전문은 [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md) §철칙.

| 규칙 | 요지 |
|---|---|
| **티어드 네거티브** | gpt-image-2는 장면 네거티브("no crowd")를 오히려 그 단어로 렌더한다. 장면 배제는 전부 긍정형 재서술(Tier-0)이 기본. 예외는 두 레인뿐 — Tier-1 텍스트 렌더 가드(화이트리스트 7종, 렌더 텍스트가 있을 때만), Tier-2 화보 컴플라이언스 페어(명시 선언 시만, 정본은 `editorial-hwabo.md` §3 한 곳). 화이트리스트 밖 부정문은 검증기가 전부 잡는다. |
| **SD 폐기 어휘 금지** | `masterpiece / 8k / trending on artstation`, 가중치 `(word:1.3)`, `--ar` 플래그도, "예쁘게·고급스럽게·어워드 수준으로" 같은 빈 형용사도 노이즈다. 수치·몸 반응·구체 예시로 환원한다. |
| **사이즈 락** | codex(`$imagegen`) 경로는 6종만 안전 — 1:1 `1024x1024` · 2:3/3:4/4:5 `1024x1536` · 3:2/4:3 `1536x1024` · 16:9 `1792x1024` · 9:16 `1024x1792` · 밀집/다컷 `2048x2048`. `auto` 금지, 프롬프트 앞머리 `[AR ...]` 브래킷 금지, 끝에 `AR x:y` 토큰 하나만. |
| **글자 후처리 절대 금지** | 텍스트는 프롬프트로 이미지 안에서 렌더한다(따옴표 카피 + 롤 라벨 + 자유 작성 존). 생성된 PNG 위에 코드로 글자를 합성(PIL·ImageMagick·SVG)하면 폰트·커닝·톤이 겉돈다. 글자 오류는 프롬프트 수정 후 재생성으로만 고친다. |
| **장비 스펙 → 결과 서술** | 모델은 `Canon R5 f/1.4`를 모른다. "shallow DoF, background falls off softly"처럼 결과로 쓴다. |
| **수치를 박는다** | HEX 팔레트(컷당 3–5색), 켈빈, `key:fill 1:2`. |
| **1행 = 1컷 = 1 호출** | 한 캔버스에 여러 컷을 그리드로 그리지 않는다. 여러 컷은 N행으로. |

## 베스트 컷

| TP8 · 리퀴드 크롬 (녹아) | TP13 · 아나모픽 착시 (LOOK) | TP14 · 미크로그래피 (고요) |
|---|---|---|
| ![TP8 리퀴드 크롬 — 녹아](docs/showcase/TP08.webp) | ![TP13 아나모픽 착시 — LOOK](docs/showcase/TP13.webp) | ![TP14 미크로그래피 — 고요](docs/showcase/TP14.webp) |
| **오클루전 × 그림자 서사 (집)** | **마스킹 × 타이포-환경 (폭풍)** | **L9 그림자 서사 (필름카메라)** |
| ![오클루전 × 그림자 서사 — 집](docs/showcase/PR07.webp) | ![마스킹 × 타이포-환경 — 폭풍](docs/showcase/PR08.webp) | ![L9 그림자 서사 — 필름카메라](docs/showcase/HD01.webp) |

갤러리 전체(전후 비교 21페어·TP 14종·P 12컷·L9 12컷) → [데모 사이트](https://gongnyang.github.io/gongnyang-prompt-kit) · 고밀도 도표 대표컷은 [`examples/diagram-gallery/`](examples/diagram-gallery/)

## 구조·릴리스·라이선스

SKILL.md에는 항상 로드되는 코어만 두고, 깊은 디테일은 `references/`로 분리했다(progressive disclosure).

<details>
<summary><code>skills/image-prompt/</code> 트리 전체</summary>

```
skills/image-prompt/
├─ SKILL.md                      # 코어 — 워크플로우·단일 라우팅 표·철칙·포맷 A/B·사이즈 락·검증기
├─ references/                   # 라우팅 표가 가리킬 때만 읽는 깊은 내용
│  ├─ category-patterns.md       #   C1–C12 컷타입·기본 AR·만화·키아트·덱
│  ├─ look-presets.md            #   룩 프리셋 L1–L9 드롭인
│  ├─ promo-router.md            #   홍보판촉물 라우터(P1–P8)·마감 디바이스·크로스브리드
│  ├─ promo/                     #     P1–P8 패턴별 드롭인 (라우터가 고른 1개만 로드)
│  ├─ typo-poster-router.md      #   타이포 포스터 라우터(TP1–TP14)
│  ├─ typo-poster/               #     TP1–TP14 패턴별 드롭인 (라우터가 고른 1개만 로드)
│  ├─ concept-axes.md            #   컨셉 축 — 사조 M1–M10·몸 반응 번역·모순쌍·컬러 번역·타이포 아트 T1–T5
│  ├─ typography-layout.md       #   영역 문법·롤 라벨·폰트 어휘·그리드
│  ├─ editorial-hwabo.md         #   화보 Format B·슬롯 12종·Tier-2 정본(§3)
│  ├─ jsonl-and-examples.md      #   jsonl 스키마·모델 팩트·codex 호출 골격
│  ├─ photo-vocab.md             #   카메라·조명·필름·구도·색 어휘 + 국문/영문 혼용
│  └─ style-taxonomy.md          #   패션 21종 + persona DNA
└─ scripts/
   ├─ check_prompt.mjs           # 티어 인식 검증기 (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # 회귀 테스트 픽스처
```

</details>

변경 이력·검증 실측 → [GitHub Releases](https://github.com/gongnyang/gongnyang-prompt-kit/releases) · 릴리스 체크리스트 [`RELEASING.md`](RELEASING.md) · 라이선스 [MIT](LICENSE)

---

<div align="center">
<sub>🐾 막연한 한마디 → 완성 프롬프트 — <a href="https://gongnyang.github.io/gongnyang-prompt-kit">gongnyang.github.io/gongnyang-prompt-kit</a></sub>
</div>
