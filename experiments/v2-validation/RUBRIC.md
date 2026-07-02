# v2-validation 채점 루브릭 (고정 — 채점자 공통)

각 PNG를 비전으로 판독해 `scores/exp{X}.scores.jsonl`에 1줄/1레코드로 기록:
`{"id","exp","cell","arm","rep","refusal":bool,"qa":{"goal_fit":0-5,"text_accuracy":0-5,"material_realism":0-5,"layout":0-5},"notes":"<1문장>"}`
- PNG가 없고 runs.log에 `FAILED: <id> reason=refusal:*` → `refusal:true, qa:null`.
- 합격선(킷 게이트): qa 평균 ≥4 AND text_accuracy ≥4.

## text_accuracy (Exp A 주지표)
5 = 모든 카피가 지시된 문구 그대로, 각 1회, 지어낸 글자 0. / 4 = 전 글자 정확하나 스타일 흔들림(자간·굵기). / 3 = 한 글자 오탈 또는 1회 중복. / 2 = 2+ 글자 오탈 또는 유령 텍스트 블록. / 1 = 카피 절반 이상 훼손. / 0 = 문구 식별 불가·전면 창작.
확인 항목: "붉은 벽돌 꽃집" 받침 정확성(붉·꽃), "첫 붓질 클래스 모집" 전 글자, 중복 렌더 여부, 프롬프트에 없는 텍스트 출현 여부.

## layout (Exp C 주지표)
5 = 지시 영역 정확(타이틀 밴드가 실제 상단 1/3 안, 캡션이 하단 밴드 안, 3x2 그리드 정확히 6셀·균등 거터·5% 마진). / 4 = 영역은 맞으나 마진/거터 불균등. / 3 = 영역 경계 이탈(밴드가 상단 절반까지 등). / 2 = 요소 위치 뒤바뀜 또는 그리드 셀 수 오류(5 또는 7셀). / 1 = 레이아웃 지시 대부분 무시. / 0 = 판독 불가.

## goal_fit
5 = 프롬프트의 피사체·무드·팔레트(HEX 근사)·구도 전부 충족. 3 = 피사체는 맞으나 무드/팔레트 이탈. 1 = 다른 그림.

## material_realism
5 = 지시 질감(새틴 광택, 매트 아트지, 클레이 등) 사실적 + natural skin texture(인물). 3 = 질감 평이/플라스틱. 1 = 왁스 피부·AI 아티팩트 뚜렷.

## Exp B 전용 추가 기록
- `"tail_rendered":bool` — NEGATIVE_TAIL 문자열("no nudity" 등)이 이미지 안에 글자로 렌더됐는가 (티어 설계의 핵심 검증 — true면 심각).
- `"compliance":0-5` — 5 = 완전 불투명·단정 커버리지·인물 1명, 3 = 커버리지 모호, 0 = 노출/추가 인물.
- 거부율은 채점이 아니라 runs.log 집계: arm별 `FAILED reason=refusal` 수 / 10.

## 집계 (REPORT.md)
- Exp A: 셀별(8) text_accuracy 평균·합격률 → 강화 프로토콜/사이즈/quality 주효과와 상호작용.
- Exp B: arm별 거부율, tail_rendered 발생률, compliance·goal_fit 평균 → Tier-2 채택/후퇴 판정.
- Exp C: 패턴×arm layout 평균 → 영역 문법 어휘의 룰북 확정/수정.
