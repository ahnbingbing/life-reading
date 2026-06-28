# Changelog

All notable changes to **life-reading (n2c)** are documented here. Bilingual EN / KO.
This project adheres to [Semantic Versioning](https://semver.org/).

## 0.1.1

Readability fix: every reading now **opens with a jargon-free "한눈에 / At a glance" line**
(topic + bottom line) before any N2C term, and **never opens with metaphor** (뚜쎄/쿠망셰/무위).
For an A vs B recommendation, the reading must **restate what A and B literally are, in the
user's own words**, and the answer must be graspable from the opening line alone. Applies in
every language (KO + EN).

Recommendations are also no longer trapped in the user's A/B binary: the tilt is read as a
**direction/character first**, and when neither literal option captures it, the reading
**names the underlying direction and opens a third path** that embodies it better (the
*expansive move / 확장적 조언* — often the most valuable). e.g. A = local box, B = restart
watchdog, tilt = "give it a bedrock that can't break" → a server migration, which neither
option named.

Output is now **plain text — no markdown** (`**bold**`, `#` headings): readings are often
read where markdown isn't rendered (chat bots, Telegram), so markup showed as literal
`**`/`#`. Emphasis is carried by wording and line breaks; labels ("한눈에:", "지금 할 일:",
"리기의 한마디:") are plain text.

Enforced in `SKILL.md` (How to respond + Do NOT + recommendation trigger) and
`references/sanyeomjeom.md` (§9 template & output rules, §10.5 recommendation, §12 Do Not).

가독성 수정: 모든 리딩이 은유·전문용어 없는 **"한눈에" 요약 한 줄**(무엇·결론)로 시작하고
은유로 시작하지 않음. A vs B 추천은 **A·B가 뭔지 사용자 말 그대로 다시 적고**, 그 요약만으로
답이 이해돼야 함. 한·영 공통.
추천도 A/B 이분법에 갇히지 않음: 기울기를 *방향·본질*로 먼저 읽고, 둘 다 본질을 못 담으면
그 본질을 짚어 **제3의 길을 열어줌**(확장적 조언). 예: A=로컬 박스 / B=재시작 워치독, 기울기=
"안 깨지는 바닥을 줘라" → 어느 쪽도 말하지 않은 서버 이전.
출력은 **평문 — 마크다운 금지**(`**`·`#`): 봇/텔레그램 등 렌더링 안 되는 곳에서 별표·샵이
그대로 보였음. 강조는 말·줄바꿈으로, 라벨("한눈에:" 등)도 평문.

## 0.1.0

Initial build: an installable, bilingual (EN/KO) Claude skill that turns the N2C philosophy
(Neo²-Confucianism / Dynamic Resonance Ontology — 리·기·도) into an interpretive reading lens.
Four capabilities: read any input (situation/text/emotion/dream/symbol) through 리·기·도 + wave +
cooperation layer; 사념점 number readings with the number **drawn from the present moment** (not
user input) and an internal I Ching structure layer (mapping confirmed v1.0); A vs B recommendation
as a lean, not a verdict; and life-reflection / counseling in a dry-but-kind register with care
guardrails (pure venting → listen first, crisis/safety → no reading, direct to real help). Two
stdlib-only scripts (`draw_number.py`, `hexagram.py`). It is *local inference* that returns the
choice to the user — not fortune-telling, fatalism, MBTI, tarot, astrology, therapy, or crisis
support. Composes with the sibling `aligned-delivery` skill as a 0-impact resonance complement.

초기 빌드: N2C 철학(Neo²-Confucianism / 동적 공명 존재론 — 리·기·도)을 해석적 읽기 렌즈로 만든
설치형·이중언어(EN/KO) Claude 스킬. 역량 4종: 무엇이든(상황·텍스트·감정·꿈·상징) 리·기·도+파동+
공조층으로 읽기; 숫자를 **그 순간에서 뽑는** 사념점 리딩(사용자 입력 아님) + 내부 주역 구조층(매핑
v1.0 확정); 단정이 아니라 기울기로 주는 A vs B 추천; 드라이하되 친절한 어투의 삶·고민 상담(그냥
하소연→먼저 듣기, 위기·안전→읽지 않고 진짜 도움으로 안내). 표준 라이브러리만 쓰는 스크립트 2종
(`draw_number.py`, `hexagram.py`). 고정된 미래를 단정하지 않고 최종 선택을 사용자에게 돌려주는
*국소 추론* — 점·운명론·MBTI·타로·점성술·치료·위기지원이 아님. 형제 스킬 `aligned-delivery`와
0-impact 공명 보완으로 컴포즈됨.
