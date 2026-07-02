# 카테고리 패턴 — C1~C12 (컷타입 · 기본 AR · 필수 디테일)

> 사용자가 카테고리·컷타입을 지정하거나 "라이브러리 스타일 변형"을 요청할 때 본다. 표현은 **긍정형 기본 + 티어 화이트리스트**(SKILL.md 철칙 #2) — 장면 배제는 "텍스트 없음"·"여백" 식 긍정 상태로, `no ~`는 Tier-1(텍스트 렌더 가드)/Tier-2(화보 컴플라이언스 페어)에서만.

**공통 시각 DNA (라이브러리 시스템 톤):** 플로팅 라벨+헤어라인 리더선 / HEX 정밀 팔레트 / 재질 매크로 / 소프트박스+림라이트 / 매거진 여백. 무드 3종 — 웜 아이보리(`#F7F4EC·#B76E79`) / 월해 다크(`#0F1D30·#1E3A5F·#B76E79`) / 테크 뉴트럴(`#F2F3F5·#11151A·#3B82F6`). 패션 에디토리얼 상세(persona DNA·Lens character·Director signature·Film 3파트)는 `style-taxonomy.md`, 결과 기반 어휘는 `photo-vocab.md`.

## C1 패션
- 컷타입: `levitation_catalog` `ghost_mannequin` `flatlay_spec` `lookbook_model` `runway_motion` `editorial_poster`
- 기본 AR: 룩북/제품 전신 `3:4`, 플랫레이 `1:1`, 포스터 `4:5`
- 필수: 의상 순서·핏·원단·액세서리 배치·바디/마네킹 노출, 필요 시 카탈로그 라벨
- 패턴: `Scene / Camera / Lighting / Color grading / Texture/Medium / Text-in-image / AR`
- **단독 인물 화보(글래머 에디토리얼)는 Format B** — 플랫 콤마형 단문, 슬롯 12종·Tier-2 문구는 `references/editorial-hwabo.md`

## C2 뷰티
- 컷타입: `texture_swatch` `water_droplet` `splash_flow` `powder_burst` `cream_smear` `hero_glow` `ingredient_macro`
- 기본 AR: `1:1` 또는 `3:4`
- 필수: 제형 질감·물방울/스플래시 물리·패키지 표면·피부/제품 접점·매크로 재질 반응
- 클린 스튜디오광·반사·성분 매크로. 하이라이트(#FFFFFF)는 "하얗게 날아가지 않게"

## C3 한국어 포스터
- 컷타입: `film_poster` `typographic_minimal` `event_promo` `cafe_menu` `exhibition` `retro_korean` `drama_poster` `editorial_quote`
- 기본 AR: `4:5` 또는 `2:3`, 모바일 포스터 `9:16`
- 필수: 정확한 한글 타이틀·부제·필요 시 장소/시간 메타·여백 시스템·타입 위계·또렷한 텍스트
- 항상 추가: "모든 텍스트는 한 번씩만, 완벽히 또렷하게."

## C4 제품 도감
- 컷타입: `exploded_view` `hero_callout` `cutaway` `comparison_grid` `blueprint` `lineup_family`
- 기본 AR: `3:4`, 가로 비교 `16:9`
- 필수: 제품 중앙·콜아웃 라벨·헤어라인 리더선·부품명·단면 재질·스케일 관계
- 도감 언어: 헤어라인 리더선, 플로팅 라벨 박스, 블루프린트 그리드, 분해 레이어

## C5 캠페인 포스터
- 컷타입: `fashion_campaign` `beauty_campaign` `cosmetic_launch` `perfume_campaign` `lookbook_cover`
- 기본 AR: `4:5`, 에디토리얼 포스터 `2:3`
- 필수: 히어로 제품/모델·캠페인 타이틀·서포팅 라인·브랜드형 비주얼 방향·여백 통제
- 히어로 하나 + 타이포 시스템 하나로 깔끔하게(과밀 피함)

## C6 인포그래픽
- 컷타입: `poster_dense`(기본) `flow_process` `cutaway` `diagram_vertical` `layered_stack` `cycle_loop` `diagram_horizontal` `comparison`
- 기본 AR: 세로 `2:3`, 가로 `16:9`
- **밀도 2모드** — 미니멀 플로우로 도망치면 맨입력보다 못해진다(실측: 4카드 플로우는 나이브 고밀도 컷에 짐).
  - **포스터형(`poster_dense`, 기본)**: 섹션 밴드 4~6개 + 섹션마다 번호·헤더, 셀마다 아이콘/미니 일러스트, **히어로 요소 1개**(실사급 렌더 — 김 나는 컵, 단면 등)를 상단 또는 중앙에, 장식 막대·게이지·미니 지도·비교표를 보조로 깔아 밀도를 채운다. 배경은 종이·크라프트·빈티지 등 질감 있는 톤. **quality high 강제 + 밀집 락 `2048x2048` 권장**(한글 정확도 레버 — 세로 비율이 우선이면 `1024x1536`, 사이즈락 6종 밖 금지).
  - **플로우형**: 단계 설명 전용(3~5스텝). 라운드 카드 + 화살표. 요청이 "단계/순서"를 명시할 때만.
- 필수: 섹션 수·읽기 순서·라벨·아이콘/다이어그램·데이터 위계. 위계는 **핵심 메시지 1개를 압도적으로 크게**, 나머지는 계단식 축소 — 시선이 큰 것→작은 것 순으로 흐르게.
- 명시 레이아웃: 번호 섹션 밴드, 화살표, 컬럼, 적층 레이어, 중앙 다이어그램, 측면 콜아웃
- **수치 가드(정확도에만 건다, 밀도에 걸지 않는다)**: gpt-image-2는 데이터를 플롯하지 못한다 — "38% 막대"는 그럴듯한 비율의 장식 막대로 렌더된다. 수치가 메시지면 **숫자를 큰 타이포로 렌더**하고 도형은 보조 장식으로. **정확히 렌더돼야 하는 카피(헤드라인·섹션 헤더·핵심 수치)만 8개 이내 따옴표 고정**, 셀 내부 디테일은 `every cell filled with genuine short Korean caption sentences, fully written in real hangul` 로 지시 — 문구를 따옴표로 고정하지 않는 **자유 작성 존**(모델이 내용을 알아서 씀, 소규모 오탈자 허용). `small caption text` 같은 추상 지시는 **밑줄 플레이스홀더 라인으로 렌더**되니 금지(실측 2026-07). 교차 화살표·다대다 연결은 뭉개진다 — 단방향 플로우·사이드 카드·리더선으로 단순화.

## C7 카드뉴스
- 컷타입: `sns_cover`(기본) `sns_content` `tip_card` `viral_hook` `qna_card` `list_card` `editorial_cover` `editorial_content`
- 기본 AR: `1:1`, 세로 에디토리얼 카드 `2:3`
- **SNS 썸네일 문법(`sns_cover` 기본)** — 피드에서 멈추게 하는 건 여백이 아니라 밀도다(실측: 매거진 여백형은 나이브 고밀도 컷에 짐).
  - 초대형 헤드라인이 **상단 40% 이상**, 핵심 키워드는 색 교체·형광 하이라이트·박스 반전으로 분리
  - 배경은 **2톤 색 블로킹**(밝은 필드 + 딥 톤 바닥) 또는 두꺼운 프레임 밴드, 브랜드 팔레트 3색 고정
  - **3D 입체 히어로 오브젝트 1개**(soft clay/plastic 렌더) + 주제 소품 3~5개(동전·계산기·영수증 류)를 하단 존에 — R축 "눈이 여기저기 튀어다니는" 드롭인과 결합해 볼거리 밀도 확보
  - **강조 장치 어휘**: 리본 밴드 · 스티커 칩 · 넘버 뱃지 · 체크리스트 미니카드 · 말풍선 배지 · 스파클 — 2~3개 골라 배치
  - 하단 페이지 인디케이터 점 3개 또는 "→" 캐러셀 신호
- `sns_content`(본문 카드): 커버보다 밀도 한 단계 낮춤 — 타이틀→불릿 2~3개→미니 일러스트의 읽기 위계, 텍스트 존/그래픽 존 분리
- 정확 카피는 헤드라인+서브 2~3개까지 따옴표 고정, 배지·칩 속 짧은 단어는 오탈자 허용 존
- 에디토리얼형(여백·매거진 톤)은 요청이 그 톤을 명시할 때만

## C8 브랜딩 목업
- 컷타입: `food_pkg` `cosmetic_pkg` `stationery_set` `signage` `app_icon_mockup` `shopping_bag` `brand_flatlay` `label_tag`
- 기본 AR: `1:1` `2:3` `16:9`
- 필수: 브랜드명·로고/라벨 배치·기재 재질·인쇄 마감·목업 표면·상업 사진
- 종이·포일·유리·플라스틱·패브릭·엠보싱·무광/유광 마감 명시

## C9 3D 아이콘
- 컷타입: `ui_component` `clay_object` `icon_set` `app_icon` `isometric_scene` `glass_icon` `emoji_3d` `logo_mark`
- 기본 AR: `1:1`, 아이콘 프레젠테이션 시트 `2:3`
- 필수: 단일 오브젝트 또는 세트 개수·재질·베벨·그림자·배경 그라데이션, 텍스트 없음(필요할 때만)
- 강한 마무리: "단일 앱 아이콘, 텍스트 없음. AR 1:1"

## C10 만화
- 컷타입: `dynamic_irregular` `page_grid` `page_4koma` `strip_vertical` `splash_page` `splash_inset` `action_spread` `page_12cut`
- 기본 AR: 페이지 `2:3`, 세로 웹툰 `9:16`, 4컷/그리드 `1:1`, 액션 스프레드 `16:9`
- 필수: 장르·퍼블리케이션 퀄리티·패널 수·거터·읽기 방향·컷별 비트·말풍선/SFX·잉킹/컬러 스타일
- 패턴: 오프닝 미디엄 문장 → 레이아웃 문장 → 컷 시퀀스 → 화풍 문장 → 팔레트 문장 → 텍스트 가독 문장 → `AR`
- 한글 대사 4~10자, 컷당 말풍선 1~2개, 다컷은 quality high·2048
- **두 전략**: (A) **멀티패널 통합 1페이지** — 캐릭터 일관성 강점, quality high·2048, 컷당 `카메라앵글+장면+감정`, establishing→close-up→reaction, 감정 피크 1회·마지막 회수, 다이나믹 레이아웃(사선거터·broken-border·cross-panel·비정형컷) 40%+. (B) **컷 단위 생성 후 조판** — 정밀 통제, 1컷=1호출, persona 블록 반복, "프레임 안엔 인물 한 명, 단독 포트레이트" 긍정 단언. 한국 웹툰(S07): soft cel shading·glossy K-beauty lips·dewy blush·vertical-scroll·3:4/4:5.

## C11 시네마틱 키아트
- 컷타입: `teaser_keyart` `character_one_sheet` `ensemble_montage` `vista_wide` `poster_2x3`
- 기본 AR: `16:9`(1792x1024) 또는 `3:2`(1536x1024), 포스터는 `2:3`(1024x1536)
- **영문 Format A 사용** — 라벨 6섹션 그대로, 본문은 영어(시네마틱 어휘 밀도가 영어에서 높음)
- 필수: **타이틀 트리트먼트용 negative space 확보**(상단 밴드 또는 중앙 여백을 Scene에 명시) · **장르별 광 레시피** — 네온 사이버펑크(practical neon glow, teal&orange, wet reflective street) / 스릴러 저조도(low key, hard rim, deep shadow pools) / 판타지 골든(golden hour volumetric light, warm haze) · **billing-block 대비 하단 여백**(하단 1/8 클린 밴드)
- 타이틀을 실제로 렌더할 땐 `typography-layout.md`의 롤 블록(headline/billing) 적용, Tier-1 결합 공식 1회
- 캐릭터 원시트는 단독 인물+콘트라포스토+림 분리, 앙상블 몽타주는 크기 위계(주연 대형·조연 중형·배경 비스타)를 명시

## C12 프레젠테이션 / 슬라이드 덱
- 컷타입: `cover_slide` `agenda_slide` `section_divider` `content_slide` `data_slide` `quote_slide` `closing_slide`
- 기본 AR: `16:9`(1792x1024) **덱 전체 고정**, 밀집 콘텐츠 슬라이드는 quality high
- 필수: **덱 DNA 블록** — 배경·팔레트 HEX·타이포 계열·장식 모티프를 한 문장으로 묶어 **전 슬라이드에 동일 문구로 반복**(시리즈 일관성의 핵심, C10 A전략의 화풍 문장과 같은 원리). 슬라이드마다 바꾸는 건 레이아웃·카피·비주얼만.
- 텍스트 예산: 슬라이드당 텍스트 블록 **4개 이하**(타이틀 + 불릿 2~3), 본문은 문장 대신 **짧은 구 단위** — 문장형 본문은 오탈자율이 뛴다(소규모 오탈자 허용 전제로 운용, 크리티컬 카피만 따옴표 고정).
- 레이아웃 패턴: `cover`(타이틀 밴드 + 풀블리드 비주얼) / `content`(좌 텍스트 컬럼 + 우 비주얼, 또는 상하 분할) / `data`(큰 숫자 타이포 중심 + 보조 도형 — C6 수치 가드 준용) / `divider`(섹션 번호 + 한 줄 타이틀, 여백 위주)
- 1행 = 1슬라이드 = 1호출. 덱은 jsonl 챕터로 관리(챕터 스키마·8섹션 변형 → `jsonl-and-examples.md` §5). 렌더 텍스트가 항상 있으므로 기본 Tier-1 승격 후보(텍스트 블록 3개+ 조건).
- 룩은 `look-presets.md`에서 1개 골라 덱 DNA 블록에 인라인한다.
