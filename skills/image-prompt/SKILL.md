---
name: image-prompt
version: "1.1.0"
description: 막연한 요청을 gpt-image-2(Codex `$imagegen`) 완성 프롬프트로 컴파일하는 스킬. 사용자의 검증된 규칙 — 네거티브 금지·전부 긍정형, 앞 브래킷 금지·끝 AR 토큰만, 장비는 결과로 환원, HEX 명시, 1행=1컷, 사이즈락 6종, C1~C10 플레이북, jsonl 스키마, 검증 스크립트. 트리거 — "공냥 프롬프트", "공냥 프롬프트 킷", "이미지 스킬", "공냥이미지스킬", "그냥 이미지 스킬", "gn-image", "gpt-image-2 프롬프트", "이미지 프롬프트 써줘", "프롬프트 라이브러리", "화보/포스터/카드뉴스/제품도감/만화 프롬프트", "프롬프트 jsonl 만들어", "프롬프트 컴파일". 후속 — "이 컷만 변형", "스타일 바꿔", "사이즈 맞춰", "한글 카피 넣어" 도 이 스킬. ※ 실제 대량 생성·스폰은 [codex-imagegen]. 이 스킬은 "프롬프트를 어떻게 쓰느냐".
---

# 🐾 공냥 프롬프트 킷 — gpt-image-2 프롬프트 컴파일러

거칠고 모호한 요청을 다운스트림 이미지 툴(`$imagegen`)에 넘길 **완성 한국어 프로덕션 프롬프트**로 바꾼다. 이미지를 직접 생성하지는 않는다(생성·양산은 **[codex-imagegen]**). 깊은 내용은 필요할 때 `references/`를 읽는다.

## 워크플로우

1. 거친 요청에서 빠진 결정(카테고리·컷타입·피사체·스타일·구도·텍스트·AR)을 **추론해 채운다**. 취향 디테일은 묻지 말고 결정. **묻는 건** 정확한 한글 문구·브랜드명·민감 소재 정도.
2. 카테고리/컷타입이 잡히면 `references/category-patterns.md`(C1~C10)를 본다.
3. 아래 **철칙**을 지켜 6섹션으로 작성, 끝에 `AR` 토큰.
4. 고가치 산출물은 응답 전 `node scripts/check_prompt.mjs <file>`로 검증(`ok:true` 확인).
5. 생성으로 이어지면 **컴파일된 프롬프트만** 넘긴다(거친 원문은 안 넘김).

**거친 입력 확장 예:** "포스터 하나"→`C3`(타이틀 위계·여백·팔레트·AR), "귀여운 아이콘"→`C9`(오브젝트·재질·베벨·배경, "텍스트 없음"), "제품 소개"→`C4`(히어로·콜아웃·리더선), "만화 느낌"→`C10`(패널·거터·말풍선·선화).

**출력 계약:** 단일 요청 → 본문 + 끝 `AR x:y`만(설명 없이). 다중 → 엔트리당 `Title / Category(Cn) / Cut type / Prompt`. 생성 요청 → 조용히 컴파일 후 이미지 툴 호출.

## 철칙 — 절대 어기지 말 것

1. **앞머리 `[AR x:y SIZE wxh]` 브래킷 금지.** size는 API 파라미터(jsonl `size`)로만. 프롬프트엔 **끝에 `AR x:y` 토큰 하나만**.
2. **네거티브 일절 금지 — 예외 없음.** `Negative:` 섹션도, 영어 `no ~`/`without ~` 부정문도 **0개**. gpt-image-2는 네거티브 단어를 오히려 렌더한다. 빼고 싶은 건 전부 **긍정형**으로 — 군중→"프레임 안엔 인물 한 명, 단독", 배경→"깨끗한 단색 배경", 워터마크→"브랜드 없는 클린 마감". 만화·뷰티·패션 동일, 구멍 없음.
3. **SD-era 폐기 어휘 금지.** `masterpiece/best quality/8k/4k/uhd/trending on artstation/ultra-detailed/highly detailed/sharp focus`. 가중치 `(word:1.3)`, 슬래시 플래그 `--ar/--v`, 본문 `§`, 빈 형용사 `멋지게/감성적으로/고급스럽게/beautiful/stunning`.
4. **장비 스펙은 노이즈 → 결과로 환원.** 카메라 EXIF·조명 장비명 대신 결과: "shallow DoF, background falls off softly", "long soft-edged shadows", "warm key + cool rim". (패션의 `Lens character:`·`Director signature:` 라인은 '결과+레퍼런스 앵커'라 예외.)
5. **수치 명세는 박는다.** HEX 팔레트(컷당 3~5색), 켈빈, `key:fill 1:2` 비율 → 품질↑.
6. **1행 = 1컷 = 1 호출.** 한 캔버스 그리드/매트릭스 금지. 여러 컷은 N개 별도 행.
7. **이상적 피부 금지** → "natural skin texture, visible pores, subtle film grain".
8. **실재 상표·인물 참조 금지** — 가상 브랜드/페르소나.

## 마스터 템플릿 (기본 6섹션 + 끝 AR)

순수 서술 + HEX. 첫 섹션이 attention을 가장 강하게 받으니 **핵심 시각정보를 최상단에**. 헤더 `# 1. Scene` 식 OK, 본문에 `§` 금지.

| # | 섹션 | 무엇을 / 분량 |
|---|---|---|
| 1 | **Scene** | 누가·무엇이·어디서·무엇을. 핵심 먼저. 60~120어 |
| 2 | **Camera** | 시점·거리·렌즈 character(결과 서술). 15~30어 |
| 3 | **Lighting** | 방향·soft/hard·그림자·림라이트(장비명 금지). 10~25어 |
| 4 | **Color grading** | 팔레트 + 색온도 + **HEX 3~5개**. 10~20어 |
| 5 | **Texture/Medium** | 매체·질감·표면 반응·후처리. 10~20어 |
| 6 | **Text-in-image** (선택) | `"따옴표 카피"` + 폰트·크기·위치 + legibility 1회. 0~25어 |
| — | 트레일링 | 끝에 `AR x:y` 토큰만 |

> jsonl 스키마·완성 예제·codex 호출 골격·8섹션 변형 → **`references/jsonl-and-examples.md`**.

## 사이즈 락 (codex 러너 6종)

API는 커스텀(최대 3840px·16배수·비율 ≤3:1)이지만 **codex(`$imagegen`) 경로는 6종만** 안전. `auto` 금지, 챕터 내 통일.

| ar | size | ar | size |
|---|---|---|---|
| 1:1 | `1024x1024` | 16:9 | `1792x1024` |
| 2:3 / 3:4 / 4:5 | `1024x1536` | 9:16 | `1024x1792` |
| 3:2 / 4:3 | `1536x1024` | 밀집/다컷 | `2048x2048` |

`2:3`만 정확비, `3:4`·`4:5`는 세로 근사 정규화. 비지원 값(`1024x1280` 등)도 가까운 6종으로.

## 텍스트 렌더 (gpt-image-2 강점, 한글 포함)

- 정확한 카피를 **따옴표로 고정**: `text reads "오늘 더 따뜻해요"`. 폰트·크기·위치·HEX 지정.
- **"appears once, perfectly legible" 1회 명시.** 같은 카피 두 번 쓰면 두 번 렌더하니 금지.
- 한 줄에 다국어 혼합 금지. 어려운 철자는 ALL CAPS/글자 풀어쓰기. 렌더 라벨엔 **실제 문구만**(플레이스홀더 금지).

## 카테고리 라우팅 (C1~C10)

컷타입·기본 AR·필수 디테일·공통 DNA·만화 A/B 전략은 **`references/category-patterns.md`**, 패션 21종은 **`references/style-taxonomy.md`**.

| C1 패션 | C2 뷰티 | C3 한국어 포스터 | C4 제품 도감 | C5 캠페인 |
|---|---|---|---|---|
| **C6 인포그래픽** | **C7 카드뉴스** | **C8 브랜딩 목업** | **C9 3D 아이콘** | **C10 만화** |

## 검증기

응답·생성 전 `node scripts/check_prompt.mjs <file>` (또는 프롬프트를 stdin 파이프). `{ok, errors, warnings}` JSON — **네거티브·앞브래킷·SD폐기어휘·가중치·슬래시플래그·끝AR누락**을 error로, 빈 형용사·HEX누락 등을 warning으로. errors 0이어야 통과. (size는 jsonl 필드라 텍스트 검증기로는 검사 안 함 — jsonl 작성 시 6종 화이트리스트 직접 확인.)

## 레퍼런스

- **`references/category-patterns.md`** — C1~C10 컷타입·기본 AR·필수 디테일·공통 DNA·만화 A/B.
- **`references/jsonl-and-examples.md`** — jsonl 스키마·완성 예제·codex 골격·8섹션 변형.
- **`references/photo-vocab.md`** — 카메라·조명·필름·구도·색 어휘(결과 기반).
- **`references/style-taxonomy.md`** — 패션 21종 + persona DNA + MASTER_TEMPLATE_V4.
- 생성·양산: **[codex-imagegen]**. 단일 1장은 그냥 codex 직접.
