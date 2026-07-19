# 🐾 공냥 프롬프트 킷 VOL.2

**막연한 한마디를 gpt-image-2 완성 프롬프트로 컴파일하는 Claude Code 스킬.**

<samp>**한국어** · [English](README.en.md) · [日本語](README.ja.md)</samp>

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) &nbsp;![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757) &nbsp;![target: gpt-image-2](https://img.shields.io/badge/target-gpt--image--2-1E4D40) &nbsp;![library: C1-C12 + P1-P8 + TP1-TP14](https://img.shields.io/badge/library-C1--C12_+_P1--P8_+_TP1--TP14-C19A6B)

![공냥 프롬프트 킷 VOL.2 키비주얼](docs/main.png)

"포스터 하나 만들어줘" 수준의 요청을 받아, 바로 생성에 넣을 수 있는 완성 한국어 프로덕션 프롬프트를 만든다. 위 키비주얼도 이 킷으로 컴파일한 프롬프트(C11 시네마틱 키아트)로 생성한 것이다.

![컴파일 데모 — 거친 요청 → 완성 프롬프트 → 검증기 통과](docs/hero.gif)

거친 요청 → 완성 프롬프트 → 검증기 통과. 이 세 단계가 스킬 안에서 끝난다. 이미지 생성 자체는 범위 밖이다 — 대량 생성은 [codex-fleet](https://github.com/kimsh-1/codex-fleet)의 `codex-imagegen` 스킬, 한 장이면 `codex`에 직접 넣는다.

> 인터랙티브 데모: **[kimsh-1.github.io/gongnyang-prompt-kit](https://kimsh-1.github.io/gongnyang-prompt-kit)**

## 무엇이 다른가 — v3 단일 라우팅 표

v3의 코어는 라우팅 표 하나다. 요청 신호를 받으면 아래 표에서 한 행을 고르고, 그 행이 가리키는 레퍼런스 파일 **하나만** 읽는다. 라우팅 정본은 [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md)의 표 한 곳뿐이며, 아래는 그 독자용 미러다.

| 이렇게 말하면 | 이렇게 컴파일된다 | 읽는 레퍼런스 |
|---|---|---|
| 단독 인물 화보·에디토리얼 | C1 · Format B 플랫 콤마형 | [`editorial-hwabo.md`](skills/image-prompt/references/editorial-hwabo.md) |
| 타이포 포스터·"글자가 곧 이미지" | TP1~TP14 중 패턴 1개 | [`typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md) → `typo-poster/` 1파일 |
| 홍보판촉물·"디자인 잘된 포스터" | P1~P8 중 패턴 1개 | [`promo-router.md`](skills/image-prompt/references/promo-router.md) → `promo/` 1파일 |
| 포스터·키아트·인포그래픽·카드뉴스·만화·도감·아이콘·뷰티·캠페인·목업 | C2~C11 | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md) 해당 절 |
| 프레젠테이션·슬라이드 덱 | C12 (16:9 기본) | [`category-patterns.md`](skills/image-prompt/references/category-patterns.md) §C12 |
| 무드("있어보이게"·"럭셔리"·"영화처럼") | 룩 프리셋 L1~L9 드롭인 | [`look-presets.md`](skills/image-prompt/references/look-presets.md) |
| 시안 다변화·"컨셉부터 잡아줘" | 컨셉 축 M1~M10 / R / X / T1~T5 변주 | [`concept-axes.md`](skills/image-prompt/references/concept-axes.md) |
| 글자 배치·폰트·그리드·밀집 텍스트 | 영역 문법·롤 라벨 | [`typography-layout.md`](skills/image-prompt/references/typography-layout.md) |
| 카메라·조명·색 어휘 | 결과 서술 어휘 | [`photo-vocab.md`](skills/image-prompt/references/photo-vocab.md) |
| jsonl 배치·모델 팩트·완성 예제 | jsonl 스키마·codex 골격 | [`jsonl-and-examples.md`](skills/image-prompt/references/jsonl-and-examples.md) |

라이브러리 커버 범위: 카테고리 **C1~C12** · 타이포 포스터 **TP1~TP14** · 홍보판촉물 **P1~P8** · 룩 프리셋 **L1~L9** · 컨셉 축 **M1~M10 / R / X / T1~T5**.

## 생성 예시 — 프롬프트가 이렇게 바뀝니다

같은 gpt-image-2다. **왼쪽은 사람이 친 한 줄을 그대로 넣은 결과, 오른쪽은 그 한 줄을 킷이 컴파일해서 넣은 결과** — 차이는 프롬프트뿐이다. 전체 컴파일 레코드는 [`examples/showcase.jsonl`](examples/showcase.jsonl).

#### `개쩌는 이미지 하나 만들어줘` → C11 시네마틱 키아트

| 스킬 없이 | 킷 컴파일 |
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

#### `재즈바 포스터` → C3 한글 포스터

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 재즈바 포스터](docs/showcase/SC03B.webp) | ![킷 컴파일 — C3 한글 포스터](docs/showcase/SC03.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

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

#### 카테고리 (C1~C10)

| 요청 → 패턴 | 스킬 없이 | 킷 컴파일 |
|---|---|---|
| `화보 한 장` → C1 화보 | ![스킬 없이](docs/showcase/SC01B.webp) | ![킷 컴파일](docs/showcase/SC01.webp) |
| `립밤 광고컷` → C2 뷰티 | ![스킬 없이](docs/showcase/SC02B.webp) | ![킷 컴파일](docs/showcase/SC02.webp) |
| `이어폰 도감` → C4 제품 도감 | ![스킬 없이](docs/showcase/SC04B.webp) | ![킷 컴파일](docs/showcase/SC04.webp) |
| `향수 캠페인` → C5 캠페인 | ![스킬 없이](docs/showcase/SC05B.webp) | ![킷 컴파일](docs/showcase/SC05.webp) |
| `커피 인포그래픽` → C6 인포그래픽 | ![스킬 없이](docs/showcase/SC06B.webp) | ![킷 컴파일](docs/showcase/SC06.webp) |
| `절약 카드뉴스` → C7 카드뉴스 | ![스킬 없이](docs/showcase/SC07B.webp) | ![킷 컴파일](docs/showcase/SC07.webp) |
| `그래놀라 패키지` → C8 브랜딩 | ![스킬 없이](docs/showcase/SC08B.webp) | ![킷 컴파일](docs/showcase/SC08.webp) |
| `로켓 3D 아이콘` → C9 3D 아이콘 | ![스킬 없이](docs/showcase/SC09B.webp) | ![킷 컴파일](docs/showcase/SC09.webp) |
| `고양이 4컷 만화` → C10 만화 | ![스킬 없이](docs/showcase/SC10B.webp) | ![킷 컴파일](docs/showcase/SC10.webp) |
| `SF 키아트` → C11 키아트 | ![스킬 없이](docs/showcase/SC11B.webp) | ![킷 컴파일](docs/showcase/SC11.webp) |

#### 룩 프리셋 (L1~L9)

| 요청 → 룩 | 스킬 없이 | 킷 컴파일 |
|---|---|---|
| `럭셔리 시계` → L1 럭셔리 에디토리얼 | ![스킬 없이](docs/showcase/SC13B.webp) | ![킷 컴파일](docs/showcase/SC13.webp) |
| `대시보드 히어로` → L5 다크 테크 | ![스킬 없이](docs/showcase/SC17B.webp) | ![킷 컴파일](docs/showcase/SC17.webp) |
| `연말 초대장` → L8 골드 포일 | ![스킬 없이](docs/showcase/SC20B.webp) | ![킷 컴파일](docs/showcase/SC20.webp) |

#### 컨셉 축 (M·T)

| 요청 → 축 | 스킬 없이 | 킷 컴파일 |
|---|---|---|
| `파도 타이포그래피 포스터` → T1 움직임 번역 | ![스킬 없이](docs/showcase/SC26B.webp) | ![킷 컴파일](docs/showcase/SC26.webp) |
| `야시장 포스터, 힙하고 키치하게` → T3 의도 왜곡 | ![스킬 없이](docs/showcase/SC27B.webp) | ![킷 컴파일](docs/showcase/SC27.webp) |
| `위스키 광고 포스터 고급스럽게` → M2 아르데코 | ![스킬 없이](docs/showcase/SC28B.webp) | ![킷 컴파일](docs/showcase/SC28.webp) |
| `록 페스티벌 포스터 멋지게` → M8 구성주의 | ![스킬 없이](docs/showcase/SC29B.webp) | ![킷 컴파일](docs/showcase/SC29.webp) |
| `향초 브랜드 포스터 예쁘게` → M7 아르누보 | ![스킬 없이](docs/showcase/SC30B.webp) | ![킷 컴파일](docs/showcase/SC30.webp) |
| `일렉트로닉 파티 포스터 힙하게` → M9 사이키델릭 | ![스킬 없이](docs/showcase/SC31B.webp) | ![킷 컴파일](docs/showcase/SC31.webp) |

## 타이포그래피 포스터 (TP1~TP14) — 글자가 곧 이미지

글자 안에 풍경을 마스킹하고(TP1), 단어를 터널로 무한 반복해 공간을 만들고(TP2), 글자를 건축물로 쌓고(TP3), 그림자와 반사가 글자를 쓰고(TP4), 유리·크롬·풍선 실물로 깎고(TP7~TP9), 분절 도색이 단 하나의 시점에서 단어로 합체하고(TP13), 수천 개의 미세 글자가 초상을 그린다(TP14). 패턴 정의는 [`typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md), 전 컷 컴파일 레코드는 [`examples/typo-poster.jsonl`](examples/typo-poster.jsonl).

| TP1 · 포토 마스킹 (SEOUL) | TP2 · 텍스트 터널 (무한) | TP3 · 타입 건축 (BUILD·WERK) |
|---|---|---|
| ![TP1 포토 마스킹 — SEOUL](docs/showcase/TP01.webp) | ![TP2 텍스트 터널 — 무한](docs/showcase/TP02.webp) | ![TP3 타입 건축 — BUILD WERK](docs/showcase/TP03.webp) |
| **TP4 · 광학 현상 (쉼)** | **TP5 · 물성 파괴 (해체)** | **TP6 · 스위스 키네틱 (will kern for food)** |
| ![TP4 광학 현상 — 쉼 그림자](docs/showcase/TP04.webp) | ![TP5 물성 파괴 — 해체](docs/showcase/TP05.webp) | ![TP6 스위스 키네틱 — will kern for food](docs/showcase/TP06.webp) |
| **TP7 · 재질 조각 (얼음)** | **TP8 · 리퀴드 크롬 (녹아)** | **TP9 · 인플레이터블 (몰랑)** |
| ![TP7 재질 조각 — 얼음](docs/showcase/TP07.webp) | ![TP8 리퀴드 크롬 — 녹아](docs/showcase/TP08.webp) | ![TP9 인플레이터블 — 몰랑](docs/showcase/TP09.webp) |
| **TP10 · 옵아트 패턴 (진동)** | **TP11 · 애시드 그래픽스 (광란)** | **TP12 · 퓨처 미디벌 (심판)** |
| ![TP10 옵아트 패턴 — 진동](docs/showcase/TP10.webp) | ![TP11 애시드 — 광란](docs/showcase/TP11.webp) | ![TP12 퓨처 미디벌 — 심판](docs/showcase/TP12.webp) |
| **TP13 · 아나모픽 착시 (LOOK)** | **TP14 · 미크로그래피 (고요)** | |
| ![TP13 아나모픽 — LOOK](docs/showcase/TP13.webp) | ![TP14 미크로그래피 — 고요](docs/showcase/TP14.webp) | |

한글 히어로 단어가 대부분의 패턴에서 그대로 성립한다 — 크롬 드립 "녹아", 풍선 "몰랑", 옵아트 "진동", 그림자 "쉼", 미세 글자 초상 "고요"까지.

## 홍보판촉물 그래픽 (P1~P8) — 디자이너 포스터 문법

카드뉴스 미감이 아니라 디자이너가 만든 홍보판촉물 톤으로 뽑는 레이어. 타이포가 장식이 아니라 피사체와 물리적으로 얽히는 8개 레이아웃 문법 + 2~3색 하드 락 + 인쇄 마감 디바이스. 룩 프리셋(L)과 직교하며 서로 교배된다. 패턴 정의는 [`promo-router.md`](skills/image-prompt/references/promo-router.md).

| P1 타이포-마스크 · 글자 안의 사진 | P2 타이포-환경 · 아이소메트릭 지형 | P3 오버사이즈 크롭 + 오클루전 |
|---|---|---|
| ![P1 타이포-마스크 — seoul](docs/showcase/PR01.webp) | ![P2 타이포-환경 — RUN 아이소메트릭](docs/showcase/PR02.webp) | ![P3 오클루전 — BREW](docs/showcase/PR03.webp) |
| **P5 메타 UI · 셀렉션 박스** | **P6 스트리트 콜라주** | **P8 모노크롬 스테이징** |
| ![P5 메타 UI — FORME 셀렉션 박스](docs/showcase/PR04.webp) | ![P6 스트리트 콜라주 — street pop](docs/showcase/PR05.webp) | ![P8 모노크롬 스테이징 — 실버](docs/showcase/PR06.webp) |
| **오클루전 × 그림자 서사 · "집"** | **마스킹 × 타이포-환경 · "폭풍"** | **빛기둥 × 스테이징 · "고요"** |
| ![집 — 입체 한 글자의 그림자가 야경 스카이라인으로](docs/showcase/PR07.webp) | ![폭풍 — 글자 안 폭풍구름, 틈으로 번개가 캔 직격](docs/showcase/PR08.webp) | ![고요 — 글자 틈으로 앰버 빛기둥이 위스키에 낙하](docs/showcase/PR09.webp) |
| **마스킹 × 셀렉션 · "소리"** | **회전축 × 마스킹 · "바다"** | **글자=책장 · "책방"** |
| ![소리 — 하프톤 군중, 한 글자만 컬러 셀렉션](docs/showcase/PR10.webp) | ![바다 — 세로 마스킹 + 90도 회전 사진](docs/showcase/PR11.webp) | ![책방 — 두 글자가 실제 책장 가구](docs/showcase/PR12.webp) |

하단 여섯 컷은 패턴 2~3개를 교배하고 한글 헤드라인으로 세운 크로스브리드 세트다. 한글 헤드라인은 마스킹·압출 모두 2글자가 안전권이다.

## 홍대 인디 무드 라인 (L9)

"있어보이는" 감성을 8개 생성 엔진으로 분해한 룩 프리셋 L9 — 단어세계 타이포(A), 사조 재해석(B), 콜라주(C), 필름 사진(D), Riso 진(E), 믹스미디어(F), 정물(G), 오브제의 그림자가 시네마틱 장면으로 번지는 그림자 서사(H).

| H · 그림자 서사 (필름카메라) | A · 단어세계 (새벽) | D · 필름 (밤) |
|---|---|---|
| ![그림자 서사 — 필름카메라](docs/showcase/HD01.webp) | ![단어세계 — 새벽](docs/showcase/HD02.webp) | ![필름 — 밤](docs/showcase/HD03.webp) |
| **B · 사조 (사이키델릭)** | **E · Riso 진 (포스터)** | **C · 콜라주 (멤피스)** |
| ![사조 — 사이키델릭](docs/showcase/HD04.webp) | ![Riso 진 — 포스터](docs/showcase/HD05.webp) | ![콜라주 — 멤피스](docs/showcase/HD06.webp) |
| **G · 정물 (와비사비)** | **F · 믹스미디어 (얼굴 몽타주)** | **D · 필름 (포장마차)** |
| ![정물 — 와비사비](docs/showcase/HD07.webp) | ![믹스미디어 — 얼굴 몽타주](docs/showcase/HD08.webp) | ![필름 — 포장마차](docs/showcase/HD09.webp) |
| **H · 그림자 서사 (위스키잔)** | **A · 단어세계 (여름밤)** | **D · 필름 (지하클럽)** |
| ![그림자 서사 — 위스키잔](docs/showcase/HD10.webp) | ![단어세계 — 여름밤](docs/showcase/HD11.webp) | ![필름 — 지하클럽](docs/showcase/HD12.webp) |

## 프레젠테이션 덱·복잡 도표 (C6·C12)

발표 슬라이드와 복잡한 개념 설명 도표도 같은 킷으로 컴파일한다 — 시퀀스 다이어그램, 다대다 네트워크, 피드백 루프, 슬라이드당 렌더 한글 400~800자의 고밀도 텍스트까지.

| 초고밀도 텍스트 (트랜스포머, ~700자) | 캐시 전략 5종 비교표 (~700자) |
|---|---|
| ![트랜스포머 아키텍처 초고밀도 슬라이드](examples/diagram-gallery/dense-16x9/DN-TRANSFORMER-001.png) | ![분산 캐시 전략 5종 비교](examples/diagram-gallery/dense-16x9/DN-CACHE-008.png) |
| **TCP 시퀀스 다이어그램 (라이프라인·교차 메시지)** | **21:9 데이터 슬라이드 (눈금·값 라벨)** |
| ![TCP 3-way 핸드셰이크 시퀀스](examples/diagram-gallery/complex-16x9/CX-TCP-002.png) | ![분기별 성장 리포트 데이터 슬라이드](examples/diagram-gallery/deck-21x9/D12-DATA-007.png) |

전체 40컷 갤러리와 원본 프롬프트 jsonl은 [`examples/diagram-gallery/`](examples/diagram-gallery/). 요점 세 가지 — 텍스트 정확도의 1차 레버는 캔버스 세로 높이(16:9·2:3에서 700~800자 안정), 크리티컬 라벨만 따옴표로 고정하고 본문 밀도는 자유 작성 존에 위임, 도표는 노드·연결·방향을 문장으로 구체 지정하면 정면 돌파된다.

## 핵심 규칙 하이라이트

잘 나오게 하는 규칙이 아니라, 안 나오게 만드는 습관을 막는 규칙이다. 전문은 [`skills/image-prompt/SKILL.md`](skills/image-prompt/SKILL.md) §철칙.

| 규칙 | 요지 |
|---|---|
| **티어드 네거티브** | gpt-image-2는 장면 네거티브("no crowd")를 오히려 그 단어로 렌더한다. 장면 배제는 전부 긍정형 재서술(Tier-0)이 기본. 예외는 두 레인뿐 — Tier-1 텍스트 렌더 가드(화이트리스트 7종, 렌더 텍스트가 있을 때만), Tier-2 화보 컴플라이언스 페어(명시 선언 시만, 정본은 `editorial-hwabo.md` §3 한 곳). 화이트리스트 밖 부정문은 검증기가 전부 잡는다. |
| **SD 폐기 어휘 금지** | `masterpiece / 8k / trending on artstation`, 가중치 `(word:1.3)`, `--ar` 플래그도, "예쁘게·고급스럽게·어워드 수준으로" 같은 빈 형용사도 노이즈다. 수치·몸 반응·구체 예시로 환원한다. |
| **사이즈 락** | codex(`$imagegen`) 경로는 6종만 안전 — 1:1 `1024x1024` · 2:3/3:4/4:5 `1024x1536` · 3:2/4:3 `1536x1024` · 16:9 `1792x1024` · 9:16 `1024x1792` · 밀집/다컷 `2048x2048`. `auto` 금지, 프롬프트 앞머리 `[AR ...]` 브래킷 금지, 끝에 `AR x:y` 토큰 하나만. |
| **글자 후처리 절대 금지** | 텍스트는 프롬프트로 이미지 안에서 렌더한다(따옴표 카피 + 롤 라벨 + 자유 작성 존). 생성된 PNG 위에 코드로 글자를 합성(PIL·ImageMagick·SVG)하면 폰트·커닝·톤이 겉돈다. 글자 오류는 프롬프트 수정 후 재생성으로만 고친다. |
| **장비 스펙 → 결과 서술** | 모델은 `Canon R5 f/1.4`를 모른다. "shallow DoF, background falls off softly"처럼 결과로 쓴다. |
| **수치를 박는다** | HEX 팔레트(컷당 3~5색), 켈빈, `key:fill 1:2`. |
| **1행 = 1컷 = 1 호출** | 한 캔버스에 여러 컷을 그리드로 그리지 않는다. 여러 컷은 N행으로. |

## 설치·사용법

```bash
git clone https://github.com/kimsh-1/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

Claude Code에서 "이미지 프롬프트 써줘", "화보 프롬프트", "키아트", "타이포 포스터" 같은 트리거나 `/image-prompt`로 실행한다. 심볼릭 링크로 설치하면 레포 업데이트가 자동 반영된다. 검증기 실행에는 Node.js가 필요하다.

작성한 프롬프트는 검증기로 검사한다. 티어를 인지해서 화이트리스트 밖 네거티브만 잡는다.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt        # 텍스트 모드
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                     # 회귀 셀프테스트
```

`{ok, format, tier, errors, warnings}` JSON을 반환한다. 화이트리스트 밖 네거티브·앞 브래킷·SD 폐기 어휘·사이즈 락 위반·슬롯 토큰 잔존은 `error`(긍정형 rewrite 힌트 포함), 빈 형용사·HEX 누락 등은 `warning`. 통과·실패 샘플은 [`examples/`](examples/)에 있다.

생성까지 이으려면 [Codex CLI](https://github.com/openai/codex) 로그인 + ChatGPT Plus/Pro가 필요하다.

## v3.0.0 — 무엇을 바꿨고 어떻게 검증했나

v3는 규칙 추가가 아니라 구조 리팩토링이다. 스킬 본문을 압축하고 라우팅을 한 곳으로 모았다.

**리팩토링 실측**

- SKILL.md 본문 17.6KB → 9.5KB
- 라우팅 3곳 중복 → 단일 라우팅 표 10행 (라우팅 정본은 SKILL.md 표 한 곳)
- frontmatter description 940자 → 316자
- Tier-2 동결 문구 전문 정본을 `editorial-hwabo.md` §3 한 곳으로 단일화
- [`RELEASING.md`](RELEASING.md) 릴리스 체크리스트 신설

**검증 실측**

- `check_prompt.mjs` fixtures **16/16 PASS**
- fresh-context 라우팅 퀴즈 **8/8** (스킬을 처음 읽는 컨텍스트에서 라우팅 표만으로 정답 도달)
- 규칙 유실 감사 **0건** — v2 규범 규칙 전수 보존 확인

**50컷 실전 테스트 (2026-07-20)**

신규 SKILL.md만 읽은 에이전트 10기가 C1~C12·TP1~TP14·P1~P8·룩/컨셉 축에 걸친 50컷을 컴파일했다.

| 단계 | 결과 |
|---|---|
| 검증기 통과 | 50/50 |
| codex(`$imagegen`) 실생성 | 50/50 성공 |
| 모더레이션 거부 | 0 |
| 소요 | 13.5분 (자동 스케일링, 피크 워커 13) |

## 구조

![공냥 프롬프트 킷 구조 — 거친 요청 → 스킬 코어 → 레퍼런스 → 완성 프롬프트 → 검증기 → 이미지 생성](docs/architecture.png)

거친 요청이 스킬 코어와 레퍼런스를 거쳐 완성 프롬프트가 되고, 검증기를 통과해야 생성으로 넘어간다. SKILL.md에는 항상 로드되는 코어만 두고, 깊은 디테일은 `references/`로 분리했다(progressive disclosure).

```
skills/image-prompt/
├─ SKILL.md                      # 코어 — 워크플로우·단일 라우팅 표·철칙·포맷 A/B·사이즈 락·검증기
├─ references/                   # 라우팅 표가 가리킬 때만 읽는 깊은 내용
│  ├─ category-patterns.md       #   C1~C12 컷타입·기본 AR·만화·키아트·덱
│  ├─ look-presets.md            #   룩 프리셋 L1~L9 드롭인
│  ├─ promo-router.md            #   홍보판촉물 라우터(P1~P8)·마감 디바이스·크로스브리드
│  ├─ promo/                     #     P1~P8 패턴별 드롭인 (라우터가 고른 1개만 로드)
│  ├─ typo-poster-router.md      #   타이포 포스터 라우터(TP1~TP14)
│  ├─ typo-poster/               #     TP1~TP14 패턴별 드롭인 (라우터가 고른 1개만 로드)
│  ├─ concept-axes.md            #   컨셉 축 — 사조 M1~M10·몸 반응 번역·모순쌍·컬러 번역·타이포 아트 T1~T5
│  ├─ typography-layout.md       #   영역 문법·롤 라벨·폰트 어휘·그리드
│  ├─ editorial-hwabo.md         #   화보 Format B·슬롯 12종·Tier-2 정본(§3)
│  ├─ jsonl-and-examples.md      #   jsonl 스키마·모델 팩트·codex 호출 골격
│  ├─ photo-vocab.md             #   카메라·조명·필름·구도·색 어휘 + 국문/영문 혼용
│  └─ style-taxonomy.md          #   패션 21종 + persona DNA
└─ scripts/
   ├─ check_prompt.mjs           # 티어 인식 검증기 (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # 회귀 테스트 픽스처
```

## 릴리스·라이선스

패턴군 추가나 규칙 변경 시의 6단계 체크리스트는 [`RELEASING.md`](RELEASING.md)에 있다 — 버전·description·라우팅 표·README 3종·설치본·검증기를 함께 갱신해야 릴리스할 수 있다.

라이선스는 [MIT](LICENSE).
