# RELEASING — 릴리스 체크리스트

새 패턴군·기능(카테고리, 룩, TP/P 패턴 등)을 추가하거나 규칙을 변경했다면, 커밋 전에 아래 6개 지점을 모두 갱신·확인한다. 하나라도 빠지면 릴리스 금지.

## 체크리스트

- [ ] **1. SKILL.md version** — frontmatter `version`을 semver로 올린다 (패턴군 추가 = minor, 규칙 수정 = patch, 구조 개편 = major).
- [ ] **2. frontmatter description** — 새 커버 영역·트리거를 반영한다. 군 이름만 열거(개별 세부 나열 금지), 체인지로그성 표현(신설·추가·vX.X) 금지, 500자 이내.
- [ ] **3. 라우팅 표** — SKILL.md의 라우팅 표에 새 요청 신호 → 카테고리/포맷 → 읽을 파일 행을 추가·수정한다. 라우팅 정본은 이 표 한 곳뿐이다.
- [ ] **4. README 3종** — `README.md` · `README.en.md` · `README.ja.md`의 구조 설명·버전 표기·SKILL.md 인용부를 동기화한다.
- [ ] **5. 설치본 동기화** — `~/.claude/skills/image-prompt`에 레포 내용을 반영한다.
  ```bash
  rsync -av --delete /mnt/d/gongnyang-prompt-kit/skills/image-prompt/ ~/.claude/skills/image-prompt/
  ```
- [ ] **6. 검증기 통과** — 테스트가 전부 PASS인지 확인한다.
  ```bash
  node skills/image-prompt/scripts/check_prompt.mjs --test
  ```

## 원칙 리마인드

- 규범 규칙의 전문 정본은 문서 1곳에만 둔다. 다른 곳은 요약+포인터.
- SKILL.md가 참조하는 경로는 전부 실존해야 한다.
- Tier-2 고정 문자열 전문은 `references/editorial-hwabo.md`(+설치본)에만 존재해야 한다(검증기·fixtures 제외).
