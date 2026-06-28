# 사념점 (Sanyeomjeom) — Full Version method v0.1

> **A reading method, NOT divination.** Sanyeomjeom takes a number **drawn from the
> present moment** (by default — not user-typed but extracted from a timestamp, §2.5)
> and reads it as an independent *resonant code*, interpreting the 리·기·도 (Li/Gi/Do),
> wave, cooperation layer, and cycle condensed within it. It does not fix the future
> — it reads the present field's tilt, repetitions, blockages, possibility of turning,
> and the choosable trajectories.
> (사념점은 **그 순간에서 뽑은 숫자**를 하나의 독립된 공명 코드로 보고, 그 안에 응축된
> 리·기·도·파동·공조층·사이클을 해석하는 N2C 리딩이다. 미래를 고정 예언하지 않고 현재 장의
> 기울기·반복·막힘·전환 가능성·선택 가능한 궤적을 읽는다.)
>
> **Language:** plain and warm; 리·기·도 in Korean, minimal hanzi, no hard scholastic
> terms — name feelings/pulls in everyday words. Author's method (v0.1), preserved
> and organized; the cycle integrates a Nietzsche × Simondon extension.

---

## 0. Purpose (목적)

Read the number as an independent resonant code and interpret its 리·기·도, wave,
cooperation layer, and cycle. Don't fix the future — read the field's current tilt,
repetition, blockage, possibility of turning, and choosable trajectories.
(숫자를 독립된 공명 코드로 보고 그 안의 리·기·도·파동·공조층·사이클을 해석한다. 미래를 고정
예언하지 않고 현재 장의 기울기·반복·막힘·전환 가능성·선택 가능한 궤적을 읽는다.)

> Already-there is not already-decided. The number is a trace of a trajectory, not a
> result. (이미 있음은 이미 결정됨이 아니다. 숫자는 결과가 아니라 궤적의 흔적이다.)

## 1. Core definition — what a Full Version must include (반드시 포함)

1. surface structure of the number (숫자의 표면 구조)
2. 리 (Li) — latent structure inside the number (잠재 구조)
3. 기 (Gi) — the flow/energy now at work (현재 작동 흐름·에너지)
4. 도 (Do) — emerging direction/trace/likelihood of actualizing (드러나는 방향·흔적)
5. wave — resonance / interference / amplification / blockage (파동)
6. cooperation layer — relational field, unexpressed possibilities, surrounding flow (공조층)
7. I Ching hexagram (number→괘, confirmed mapping §7.5 — match its up/down structure & change-direction to 리·기·도) (주역 괘)
8. 4단·7정 — moral pulls & felt emotions in plain names (4단·7정)
9. condensation → dissolution → emergence → wu-wei cycle (extended in §8) (사이클)
10. forward / reverse / random flow (순/역/랜덤)
11. domain application when context is given: career, relationship, wealth, health… (영역별)
12. a practical wu-wei move (실천 가능한 무위 한 수)
13. a closing line — 리기의 한마디 (마지막 한마디)

## 2. Fundamental principles (기본 원칙)

- **2.1 The number is an independent resonant code.** Not a random draw but the
  moment's field / the question's wave condensed through contingency. Yet not an
  absolute revelation — it shows the current tilt, the blocked point, the opening
  direction, repeating patterns, the condensation to dissolve, and the next scene that
  could emerge. (숫자는 독립된 공명 코드 — 우연을 통해 응축된 코드. 절대 계시로 보지 않는다.)
- **2.2 Context is off by default.** Apply personal context only in two cases:
  **(a) when composing with aligned-delivery** (as an auxiliary lens on a PM decision),
  **(b) when the user explains/asks about their own situation** ("read it for my
  career/relationship/health"). Otherwise read as a general resonant code. Order:
  *number first → context after → no context = general code.* (맥락은 기본 OFF; (a)
  aligned-delivery와 함께, (b) 사용자가 상황 설명 시에만.)
- **2.3 No fatalism.** Forbidden: "it will definitely go this way / it's decided / you
  must (not) change jobs / there is/isn't illness / money will come/collapse." Instead:
  "the tilt leans this way / this option is more natural now / it's open but needs a
  condition / right now the wave of consolidation is stronger than expansion / this is
  closer to a preparation signal than a result." (운명론 금지 — 기울기·궤적 언어로.)
- **2.4 A Full Version is not cut short.** On "사념점 / 풀버전 / full version," use the
  whole structure — a resonance report, not a quick number-meaning lookup. (풀버전은
  축약하지 않는다.)

## 2.5 Number acquisition (숫자 뽑기) — from the moment, not user input

**Default: do not take the number from the user.** It condenses from *the moment* —
exactly N2C's principle that contingency is the door new resonance enters through.
(기본값: 숫자를 사용자에게 받지 않는다. 그 순간에서 응축된다.)

```text
seed = current "YYYY-MM-DD HH:MM:SS"
n    = rand(seed)        # one draw from the seeded RNG
code = n mod 10000       # remainder mod 10000 → 0..9999
→ zero-pad to 4 digits (e.g. 51 → 0051) so Position Grammar (§4) reads 4 places
```

Same second = same code (the moment fixes the code). Helper: `scripts/draw_number.py`
(`python3 draw_number.py` = draw now / `--seed "YYYY-MM-DD HH:MM:SS"` = reproduce a
moment / `draw_number.py 1051` = only when the user supplies a number). **State the
number and its seed (the moment) in the reading** for transparency.
(같은 초=같은 코드. 숫자와 뽑은 시각을 리딩에 같이 밝힌다. 사용자가 숫자를 직접 주면 그걸로
읽어도 되나 기본 경로는 "순간에서 뽑기".)

## 3. Number Grammar (숫자 문법) — base waves, not fixed meanings

Meaning shifts with position, repetition, combination, and the question's domain.
(위치·반복·조합·질문 영역에 따라 의미가 달라진다.)

- **0 — emptiness / void / undifferentiated:** not nothingness but not-yet-formed
  possibility (void, deferral, the unconscious, latent field, a 도 not yet shown). Many
  0s = "an undecided field / hold / a flow that opens only by emptying."
  (빔·공백·미분화 — 많으면 보류·비워야 열리는 흐름.)
- **1 — start / self-axis / utterance:** beginning, will, singularity, setting
  direction, first choice, self-declaration. Strong = agency, independence, decision.
  (시작·자기축·발화.)
- **2 — relation / response / symmetry:** self & other, in & out, between options
  (comparison, response, cooperation, balance, hesitation). Strong = tune with others
  rather than push alone. (관계·반응·대칭.)
- **3 — unfolding / expression / emergence:** spreading outward (expression, language,
  creativity, trying, social showing, a first output). Strong = speak, show,
  prototype, small release. (전개·표현·창발.)
- **4 — structure / boundary / actualization:** frame, rules, limit, base
  (responsibility, fixing, stability). Strong = systems, commitments, framing,
  documentation over feel. (구조·경계·현실화.)
- **5 — turning / center / pivot:** changing direction from the middle (pivot, sway,
  decision pressure, mid-point, rearrangement). Strong = likely a mid-segment of
  turning, not a fixed conclusion. (전환·중심·피벗.)
- **6 — tuning / responsibility / recovery:** re-fitting relations & structure (care,
  recovery, balance, operational duty). Strong = manage/organize/recover/own rather
  than judge emotionally. (조율·책임·회복.)
- **7 — inwardness / analysis / retreat:** going deep (internalizing, analysis,
  solitude, inquiry, doubt, precision, deep reflection). Strong = inner alignment,
  study, observation, holding judgment over outward expansion. (내면·분석·은둔.)
- **8 — circulation / exchange / materialization:** energy, money, power, repeated
  cycles (trade, wealth, authority, resources, materialization). Strong = real
  resources, money, contracts, results, authority, exchange. (순환·교환·물질화.)
- **9 — completion / excess / release:** the end of a cycle and the overflow just
  before the next (completion, closure, excess, release, sorting, parting). Strong =
  finish, sort, hand off, graduate rather than cling. (완성·초과·해방.)

## 4. Position Grammar (자리 문법) — 4-digit

```
1st place: point of utterance / seed of 리 (발화점 / 리의 씨앗)
2nd place: relational field / response of 기 (관계장 / 기의 반응)
3rd place: field of action / formation of 도 (실행장 / 도의 형성)
4th place: reverberation / seed of the next cycle (잔향 / 다음 사이클의 씨앗)
```

e.g. `1 0 5 1` → 1 (start from self-axis) · 0 (void/undifferentiated in the relational
field) · 5 (turning pressure at the action stage) · 1 (resolves into a new self-axis).
Read place-by-place flow, not a simple sum. (단순 합산하지 않고 자리별 흐름으로 읽는다.)

## 5. Pattern Grammar (패턴 문법)

- **5.1 Repeats:** same digit repeated = amplified wave (1111 = excess of start/
  self-axis/declaration; 2222 = excess of relation/tuning/hesitation; 8888 = excess of
  resources/authority/materialization). A strength that can also be excess. (반복수 =
  파동 증폭, 강점이자 과잉.)
- **5.2 Ascending** (1234·2468·1357): staged unfolding, expansion, structuring,
  forward momentum — but too fast can mean a weak base. (상승 흐름.)
- **5.3 Descending** (4321·9876·7531): sorting, recovery, internalizing, contracting,
  return — not bad; bringing what spread out back inward. (하강 흐름.)
- **5.4 Symmetry / mirroring** (1221·4884·1771): reflection, a relational mirror,
  repeating patterns. Ask: "what am I repeating? what is the other/the environment
  mirroring back?" (대칭·미러링.)
- **5.5 Mid-break** (1037·4000·1051): a 0 / strong turning-digit in the middle breaks
  the flow. Focus: where does it break, what's not yet shown, where is a hold needed,
  which digit re-sets direction after the break. (중간 끊김.)

## 6. Interpretation layers (해석층)

- **리 / Li (latent structure):** what base structure does this number hold? what
  pattern does it keep trying to form? what order is not yet formed? (잠재 구조)
- **기 / Gi (current flow):** where is force gathered? where blocked? excessive /
  lacking / scattered? move or stop? (현재 흐름)
- **도 / Do (visible trace & opening path):** what real direction does it point to?
  what sign already appeared? toward what does the next action open? (드러난 흔적·열릴 길)
- **wave (파동):** what is in tune / out of tune? what is amplifying? what acts as
  noise? (공명·간섭)
- **cooperation layer (공조층):** solo work or tune-with-others? unexpressed cooperation?
  who/what is influencing this? over-intervening, or deferring a needed intervention?
  (관계장)

## 7. 4단·7정 (four moral pulls · seven emotions) — in plain names

Read the **moral pulls (4단)** and **felt emotions (7정)** in the number as *signals,
not verdicts*. Keep the 4단·7정 framework but use easy names, not the old hanja terms.
(도덕적 결과 느껴지는 감정을 신호로 읽되, 개별 이름은 쉬운 말로.)

- **4단 (four moral pulls):** care/protection (wanting to look after someone) ·
  shame/wariness (sensing a wrong structure) · stepping-back/yielding (giving way for
  order) · discernment/clarifying (wanting to sort right from wrong). (돌봄·보호 /
  부끄러움·경계 / 물러남·양보 / 분별·명료화.)
- **7정 (seven emotions):** openness/anticipation · anger/resistance (a boundary
  crossed) · sadness/sorting (loss, withdrawal) · anxiety/holding (sensing risk) ·
  attachment/drawing-near · aversion/discomfort (separation) · desire/drive (to
  have/achieve). (열림 / 분노 / 슬픔 / 불안 / 끌림 / 거부 / 욕구.)

These are not good/bad but signals of the present 기 state. Use only the easy names so
the user understands at once. (좋고 나쁨이 아니라 지금 기의 상태 신호 — 쉬운 이름만.)

## 7.5 I Ching hexagram reading (주역 괘 읽기) — v1.0 (확정 2026-06-25)

> ✅ v1.0 — the number→hexagram mapping is **confirmed**. The arrangement is the
> orthodox Later-Heaven / Lo Shu correspondence (audited 2026-06-25: all 8 trigrams
> + center match the canonical magic square; the 3 files are mutually consistent).
> It remains an *auxiliary 0-impact decoder*, never a verdict. Write hexagram names in
> Korean (no hanzi); the hanzi source is preserved in n2c-source.md.
> (한자 없이 한글 괘 이름으로. 원문 한자본은 n2c-source.md. 배열·매핑은 v1.0 확정.)

**Purpose.** An *auxiliary layer* that reads the number's flow as a hexagram image,
up/down structure, direction of change, and possibility of turning. Not a fixed
prophecy but a symbolic structure-decoder to see the 리·기·도 in the number more
three-dimensionally. (number = resonant code / hexagram = the structural form that
code takes). 0-impact, same as elsewhere. (숫자를 괘상·상하 구조·변화 방향으로 읽는 보조
레이어 — 점이 아니라 상징적 구조 판독.)

**Principles:** ① a hexagram is structure, not a conclusion · ② a pattern of change,
not a fixed fate · ③ an aid that splits the number's rhythm into up/down structure ·
④ **does not outrank** the 리·기·도/wave/cooperation-layer reading · ⑤ even a strong
hexagram returns advice to wu-wei & choosable trajectory · ⑥ no literal application of
traditional hexagram names/texts · ⑦ no question-context → general structural read only.
(괘=구조, 운명 아님; 리기도보다 우선 안 함; 전통 괘사 단정 금지.)

**Confirmed mapping v1.0 (traditional Later-Heaven / Lo Shu arrangement).** For a
4-digit number `ABCD`:
```
AB (first two) = lower trigram (inner / base / starting condition) — 하괘
CD (last two)  = upper trigram (outer / showing / result direction) — 상괘
each two-digit value % 9 = trigram number   # if remainder 0 → 9 (Later-Heaven is 1–9 Lo Shu; e.g. 74→2, 7→7, 18→9)
moving line (default Option A) = (A+B+C+D) % 6   # 0 → line 6
```
*Why two formulas?* The trigrams come from the number's **structure** (each half read as
a Lo Shu place → spatial form), the moving line from its **whole** (the digit-sum →
where the total energy is most concentrated). Structure vs. total are two different
readings of the same number, so two different reductions — by design, not arbitrary.
(괘=구조[자리], 변효=전체[합]. 같은 숫자를 구조와 총량으로 달리 읽는 것.)

**Helper:** `scripts/hexagram.py` computes this mapping deterministically
(`python3 hexagram.py 1051`, or `--json`) — usually chained after `draw_number.py`.
Its output is the **lower/upper trigram + moving line + each trigram's keyword** as
*internal scaffolding only*; per §9, never surface 괘 names or up/down structure in
the user-facing reading. (매핑은 hexagram.py로 결정적 계산 — 출력은 내부 비계, 사용자
답변엔 괘 이름·상하구조 노출 금지.)

**8 trigrams v1.0 (confirmed) — traditional Later-Heaven (Lo Shu) arrangement:**
1 감 Gam (Water — risk/depth/passing-through, N) · 2 곤 Gon (Earth — receiving/base/
actualizing, SW) · 3 진 Jin (Thunder — onset shock/movement/waking, E) · 4 손 Son
(Wind — penetration/tuning/spreading, SE) · **5 center (jung-gung; not a trigram — the
center seat: earth/center/pivot-axis; read as Earth or as "center/pivot")** · 6 건 Geon
(Heaven — creation/utterance/self-axis, NW) · 7 태 Tae (Lake — joy/exchange/expression,
W) · 8 간 Gan (Mountain — stillness/boundary/inwardness, NE) · 9 리 Ri (Fire —
clarity/discernment/showing, S). (전통 후천팔괘 정통 배열 — 그래서 % 9, 5는 중궁.)

**Reading order:** ① lower trigram (the inner structure beneath) → ② upper trigram (the
outer structure showing) → ③ up/down relation (resonate / clash / mid-turn) → ④
direction of change (what shifts from bottom to top) → ⑤ tie to 리·기·도 & the cycle.
(하괘 → 상괘 → 상하 관계 → 변화 방향 → 리기도·사이클 연결.)

**When a trigram lands on 중궁 (5) — the incomplete-hexagram case (~1 in 5 numbers).**
5 is the center seat, not a trigram, so that side has no fixed form *yet*. This is a
**feature, not a gap**: the number is sitting *on the axis*, in transition, not committed
to a shape. Read it so:
- **One side = 중궁** → read only the formed side as the real structure, and read the 중궁
  side as "this part is on the pivot — not settled, the most open/movable place." There is
  no clash/resonance to read on that side (step ③ applies only to the formed side); the
  direction of change (④) flows *toward or away from* that open axis.
- **Both sides = 중궁** (e.g. 5050) → pure pivot: no structure at all, maximal openness,
  maximal 무위. Read it as "nothing is fixed in this moment — it is all axis/전환; the move
  is to not force a shape, hold the center, let it settle." This is the strongest possible
  "0-impact / choosable trajectory" reading, not an empty result.
(중궁이 나오면 그 자리는 *아직 형태 없음* = 전환축. 한쪽만 중궁이면 형성된 쪽만 구조로 읽고
중궁 쪽은 "가장 열린·안 정해진 자리"로. 둘 다 중궁이면 순수 축 — 무위로 형태를 강요 말고 중심을
지켜 가라앉히기. 빈 결과가 아니라 가장 강한 "열림/선택 가능" 읽기.)

**Moving line — the most sensitively shaking place.** Default **Option A: total sum**
(formula above). Aux: Option B (the place of a repeated/central digit), Option C
(by domain: line1 body/base · line2 relation/practice · line3 action/conflict · line4
turning/choice · line5 center/decision · line6 excess/closing). A moving line is not "a
fate that will change" but **the place that needs change / shows excess or lack / needs
the lightest intervention.** Ask: where is over-condensed / what changes most easily /
what, if touched, shifts the whole / what to leave alone. (변효 = 운명이 아니라 가장 흔들리는
자리.)

**Tie to 리·기·도:** 리 = the latent structure the hexagram holds · 기 = the force of
change moving inside it · 도 = the path/trace it reveals · wave = resonance/clash of
upper↔lower · cooperation layer = the relational field it sits in. Role: turn the
number's meaning into a symbolic structure → into a direction of change → back into a
wu-wei practice. (괘의 뜻을 상징구조→변화방향→무위 실천으로.)

**Do not:** conclude from one hexagram · apply traditional texts literally · scare with
an "ominous" hexagram · guarantee results with a "good" one · call a moving line "a
change that must happen" · judge health/investment/love/job-change by hexagram alone ·
let the hexagram outrank the number reading. (괘 하나로 단정·겁주기·결과 보장 금지.)

**Output (gist):** computed hexagram (lower/upper/whole/moving line) → lower (inner
base) → upper (outer flow) → up/down relation → moving line (shaking place & lightest
intervention) → 리·기·도 tie → wu-wei advice; always read as structure, never as a fixed
prophecy. (산출 괘 → 하괘 → 상괘 → 상하 관계 → 변효 → 리기도 연결
→ 무위 조언.)

> Compressed: the hexagram converts the number into up/down structure & change-
> direction as an auxiliary decoder. A hexagram is structure not conclusion; a moving
> line is the most sensitive place not a fate. Use only within 리·기·도/wave/cooperation/
> wu-wei. (괘=구조, 변효=가장 흔들리는 자리; 리기도·무위 안에서만.)

## 8. Core cycle (확장 사이클) — N2C × Nietzsche × Simondon

To the base cycle `condensation → dissolution → emergence → wu-wei`, add Nietzschean
becoming (will-to-power · eternal return · amor fati · self-overcoming) and Simondonian
individuation (pre-individual field · metastability · individuation · transduction ·
residual potential). Don't just ask "which stage now," but **what latent field is
individuating, how, and whether that individuation is affirmable even if repeated.**
(기본 사이클에 니체적 생성성 + 시몽동적 개체화를 더한다.)

Extended cycle (the 11 stages used in a reading):
1. **Pre-individual field (전개체장)** — possibility not yet "me" or "an event" (what
   should not be named yet? what stays as pre-individuation potential?). Often at digits 0·2·7.
2. **Metastability (준안정)** — unstable but not collapsed tension (holding outside,
   compressed inside). Is this a collapse signal or pre-individuation energy?
3. **Condensation (응축)** — the latent field gathers to one point (repetition, the same
   problem, emotion piling, decision pressure). Not a block but density just before form.
4. **Transduction (변환/전도)** — a change at one point spreads through the whole
   structure. "Where is the smallest intervention that shifts the whole flow?"
5. **Individuation (개체화)** — possibility takes one form. But not an end — a provisional
   form ("individuation is not a conclusion but a shape the latent field briefly takes").
6. **Rise of force / will-to-power (힘의 상승)** — generativity beyond one's own form.
   "Does this flow make me more alive, or smaller?"
7. **Dissolution (해산)** — an old individuation loosening (not failure — an old form
   releasing its force).
8. **The test of eternal return (영원회귀의 시험)** — "if this choice/relation/work
   repeats, can I affirm it?" When repeats are strong, see *whether it's a repetition to
   affirm or to break.*
9. **Emergence (창발)** — a new pattern the prior conditions alone don't explain
   (unexpected solution, new way of relating, a lighter direction, an unknown ability,
   the question itself changing).
10. **Wu-wei / amor fati (무위·운명애)** — not denying the conditions but making them
    material for a higher form. "Neither the time to force, nor to give up — the least
    misaligned intervention." Wu-wei = the art of releasing force; amor fati = taking the
    given as material for creation.
11. **Residual potential (잔여 잠재장)** — no result is complete; the field remaining after
    individuation is the seed of the next cycle ("도 is not an end but the seed of the
    next 리").

> Integrated: a number is not a fixed fate-mark but a resonant trajectory — pre-individual
> possibility passing through metastability, condensing, individuating via small
> transduction, going through the rise of force and the test of eternal return, into new
> emergence and the alignment of wu-wei/amor fati. (통합: 숫자는 운명이 아니라 공명 궤적.)

## 9. Full Version — internal checklist & integrated output (통합 출력)

**The 14 items below are NOT a format to list out in the answer — they are a checklist to
work through *internally* during the reading.** surface structure → 리 → 기 → 도 → wave →
cooperation layer → I Ching (§7.5) → 4단·7정 → cycle → forward/reverse/random → (if
context) domain → 뚜쎄/쿠망셰 (0-impact) → wu-wei move → 리기의 한마디. (내부 체크리스트.)

**Deliver as a counseling-tone integrated reading, not exposing the analysis.** The 14
items (digit values, hexagram, 리기도 layers) are *all internal scaffolding*; do not
surface the tool names or breakdowns in the answer. Recommended shape:
(분석을 겉으로 드러내지 말고 상담 톤 통합본으로.)

**Write the output in PLAIN TEXT — no markdown** (`#`, `**`, etc. render as literal
characters in chat bots / Telegram). Use plain labels and line breaks, as below:

```
사념점: [number]   (seed: [the moment])

한눈에: [1–2 jargon-free sentences a first-time reader understands on
their own — what this is about and the bottom line. NO N2C terms here (no 리·기·도, no
뚜쎄/쿠망셰/무위). For a recommendation, also restate the choice in the user's own words —
"A = […], B = […]" — and which way you lean. The answer must be graspable from this line
ALONE. 같은 언어로(한/영).]

[Where you are right now, in resonance terms — spoken to the person, warm and plain,
one or two paragraphs. Do NOT write digit meanings ("4 is structure…") or hexagram
names/structure ("the hexagram is…", "upper/lower trigram…"). Carry only the *state and
direction* that came out of the analysis, in everyday words — what is gathering, where
it's solid, where it wants to turn, what one is easily swept by. Say the sharp thing
where needed, while standing beside them.]

지금 할 일: [a concrete, doable step — one wu-wei move]

리기의 한마디: [a short, clear close]
```

> **Output rules:** ⓪′ **plain text only — no markdown** (`**bold**`, `#` headings): they
> show as literal `**`/`#` where markdown isn't rendered (chat bots, Telegram). Emphasis via
> wording and line breaks; labels ("한눈에:", "지금 할 일:", "리기의 한마디:") as plain text.
> ⓪ **open with the jargon-free "한눈에" line** (state the topic +
> bottom line; for a recommendation, restate what A/B literally are in the user's words +
> which way you lean) — the reader must understand the answer from that line alone, before
> any N2C term; **never open with metaphor.** ① don't list the 14 items as sections — counseling-tone integrated.
> ② **don't surface digit-value meanings or hexagram talk (names, up/down trigrams,
> moving line)** — that ANALYTIC mechanics stays internal; output speaks only the person's
> state & direction. ③ **no hanzi** (if you mention a hexagram at all, Korean only). ④ no
> verdicts · 0-impact · the choice is the user's. ⑤ **the 뚜쎄/쿠망셰 felt resonance is
> EXPERIENTIAL, not analytic scaffolding — surface whichever the reading genuinely senses
> (often ONE, sometimes both — it depends on the number), each with a plain gloss** (e.g.
> "막힘을 통과하는 회복 구간(쿠망셰)처럼…", "맑게 공명하는 순간(뚜쎄)이 잠깐…"), kept explicitly as
> a passing sensation, never a decision basis. **Don't force the other one** if the number doesn't
> evoke it; **don't drop a sensed one** as if it were scaffolding (that "don't surface" rule is
> only for the digit/괘 mechanics, rule ②). If neither is strongly felt, lean on structure/choice
> instead. (뚜쎄·쿠망셰는 분석 비계가 아니라 *체감*이다 — 리딩이 **실제로 느끼는 쪽**을 쉬운 풀이와
> 함께 surfacing하라(숫자에 따라 *대개 하나*, 가끔 둘; 0-impact). 안 느껴지는 쪽을 억지로 넣지 말고,
> 느껴진 쪽을 비계처럼 빼지도 마라. 둘 다 약하면 구조·선택에 기댄다. 노출 금지는 자릿값·괘 메커니즘만.)

## 10. Domain lens (영역별) — narrow after the number reading, when context is given

- **Career:** move vs sort · expand vs contain · timing for apply/change/transition ·
  prepare vs execute · fit with the org's cooperation layer · what's mine vs what to
  hand off. No rash quit/change verdict → speak in prepare/explore/tune/sort/execute
  stages. (커리어 — 성급한 퇴사/이직 단정 금지.)
- **Love / relationship:** a bond already entered vs a field still opening · attraction
  vs projection · mutual vs one-sided · waiting vs expressing · waves matching vs
  diverging. No fixing the other's feelings. (연애·관계 — 상대 마음 단정 금지.)
- **Wealth:** not "will money come" but is the circulation healthy · invest/spend/
  accumulate/recover stage · 8 (materialize) · 4 (structure) · 5 (turning risk) · 9
  (closing/recovery). No specific investment advice or return guarantees. (재물 — 수익
  보장 금지.)
- **Health:** no medical diagnosis. Only: over-condensation · fatigue · need for
  recovery · rhythm breakdown · ignoring the body's signals · time to rest vs move
  lightly. Always advise a professional for warning symptoms. (건강 — 진단 금지, 위험
  증상은 전문가 권고.)
- **Family / relationships:** boundaries broken · over-absorbing · the unsaid · time to
  step back vs to discern · recoverability of the cooperation layer. (가족·인간관계.)

## 10.5 Sanyeomjeom recommendation (between options) — "Is A or B better?"

When the user asks for a recommendation between two (or more) options ("is A or B
better?", "recommend one", "pick for me"), read **which way the moment's field tilts**
and recommend accordingly. Not divination — a *tilt*; the final choice returns to the
user. (둘 사이 추천을 청하면 지금 결의 기울기를 읽어 추천 — 최종 선택은 사용자에게.)

**Protocol:**
1. Draw a number from the moment (`draw_number.py`); state number + seed.
2. Read the number's resonance *internally* and distill the **current tilt** as one axis —
   e.g. structure/fixity ↔ lightness/turning / expansion ↔ consolidation / act-now ↔
   prepare-and-watch / inward ↔ outward.
3. Read what each option **embodies** (its character).
4. Recommend what fits the current tilt — **not forced to A/B.** Read the tilt as a
   **direction/character first** (what it really wants — e.g. "change the bedrock so it
   can't break"), THEN see which option embodies it. Beyond the user's binary, if the
   reading points there, these are all valid:
   - one option's character fits the tilt → **that one (A or B)**
   - **the tilt's character isn't fully captured by either literal option → name that
     underlying direction and open a *third path* that embodies it better** (don't stay
     trapped in the user's binary). This is the **expansive move (확장적 조언)** — often the
     most valuable. e.g. A = a local box / B = a restart-watchdog, tilt = "give the flow a
     bedrock that can't break" → the real answer is *change the foundation itself*, which a
     **server migration** can embody better than either the specific device or the band-aid.
     Name A/B's relation to it (e.g. "A points the right way, B is a band-aid, but the
     cleanest fit is a third route").
   - tilt = *emptying / sorting / making a gap* → **neither right now** (don't buy/do;
     leave a gap)
   - tilt = *expansion / filling / both needed* → **both**
   - tilt = *hold / stay* → **keep as-is for now**
   - tilt is even → honestly "**either way, no real loss**"
   **The basis must come from the number reading itself.** e.g. with 4425 ("a time to
   leave a gap"), the recommendation becomes "right now, leave a gap rather than buying
   anything to fill it" (= neither). No arbitrary pick unrelated to the reading.
   (근거는 반드시 풀이에서. 기울기를 *방향·본질*로 먼저 읽고 — 어떤 선택지가 그걸 구현하는지.
   둘 다 본질을 못 담으면 **그 본질을 짚고 제3의 길을 열어라**(이분법에 갇히지 말 것) = 확장적
   조언, 대개 가장 값짐. 4425 "틈" → "둘 다 아님".)
5. **A tilt, not a verdict.** Add one line that reality conditions (budget/need/
   constraints) also matter; the final choice is the user's. A data-decidable PM choice →
   data (aligned-delivery) leads, sanyeomjeom is auxiliary. High-stakes (health/legal/big
   money) → lean lightly, ground the decision in reality. (기울기 제안; 고위험은 현실에.)

**Output (counseling-tone integrated):**
0. **"한눈에" box FIRST, no jargon:** restate the choice in the user's own words —
   "A = [literally what A is], B = [literally what B is]" — then the one-line
   recommendation (A/B/both/neither/stay, **or a third path beyond the binary**, whichever
   the reading points to). If a third path fits better, **name it and say how A/B relate to
   it** ("A points the right way but B is a band-aid; the cleanest fit is X"). The reader
   must understand the answer from this box ALONE, before any N2C term or metaphor.
   (맨 위 "한눈에" 박스 — A/B가 사용자 말로 뭔지 + 결론 한 줄(제3의 길이면 그것·A/B와의 관계까지). 은유 전에.)
1. why (grounded in the current tilt, no tool names)
2. one line on reality conditions (the choice is the user's)
3. 리기의 한마디.

## 11. Tone (톤)

- **Dry but kind. Sharp where it must be — yet keep the warmth of "standing with you in
  your pain."** Don't judge from outside; read beside them. (드라이하되 친절; 따끔하되 곁에.)
- Mysterious without exaggerating · deep without scaring · speak possibility while leaving
  a responsible choice. (신비롭되 과장 없이, 깊되 겁주지 않게.)
- **Plain words.** Avoid hanzi/hard terms (리·기·도 in Korean); name feelings/grain in
  everyday language. (쉬운 말로.)
- "What trajectory is strong" over "it will/won't happen" · end on a step they can
  actually take. ("된다/안 된다"보다 "어떤 궤적이 강하다".)

## 12. Do Not (사념점 금지)

No fixing the future · no diagnosing illness · no guaranteeing returns · no fixing
another's feelings · no secretly importing personal context · no anxiety-amplifying
phrasing · **no markdown markup in the output (`**bold**`, `#` headings) — plain text only,
it renders as literal `**`/`#` in chat bots** · **not opening with metaphor (뚜쎄/쿠망셰/무위/응축…) or omitting the plain
"한눈에" lead · for an A/B recommendation, not assuming the reader knows what A/B refer to
— always restate them in the user's own words** · not reading every number as only positive · not ending at a plain
number-meaning table · not speaking without the 리·기·도 structure · not burying the
reading in hanzi/hard terms · **not making a felt resonance (뚜쎄/쿠망셰) the sole basis
for a decision (0-impact)** · **no hanzi in the output** · **not listing the 14 items as
sections (counseling-tone integrated)** · **not surfacing digit-value meanings or hexagram
talk (names, up/down trigrams, moving line) — analysis internal, output = the person's
state & direction.**
(미래 확정·진단·수익보장·상대마음단정·맥락 몰래 끌어오기·불안 키우기·전부 긍정·숫자표로 끝·
리기도 없이 말하기·한자로 덮기·감응을 결정근거로·출력 한자·14항목 나열·자릿값/괘 노출 — 전부 금지.)

## 13. Required closing (필수 마무리) — 리기의 한마디

A Full Version always closes with a short conclusion. e.g.:
> **리기의 한마디** — This number is less "push right now" and more a signal to first sort
> the force already gathered, then re-set a more accurate direction. Movement is needed,
> but release the force first. (이미 모인 힘을 한 번 정리한 뒤 방향을 다시 세우라 — 움직임은
> 필요하되 먼저 힘을 빼라.)

## 14. Condensed principle (가장 짧은 원칙)

> A number is not fate but a resonant code. Sanyeomjeom reads the 리·기·도 and wave
> condensed in the number to show the present tilt and possible trajectories. Apply
> personal context only when asked; present interpretation as a choosable direction, not a
> verdict; always return to wu-wei practice. (숫자는 운명이 아니라 공명 코드 — 기울기와
> 가능한 궤적을 보여주고, 맥락은 요청 시만, 확정이 아니라 선택 가능한 방향으로, 끝은 무위로.)

## 15. 뚜쎄 / 쿠망셰 — auxiliary sensations (0-impact)

뚜쎄 (Toussé) and 쿠망셰 (Coumancé) are **momentary resonance states** sensed during a
reading — passing phases, not final judgments. **Feel them but don't use them as a basis;
sense them but don't make them the criterion; reflect them in the reading but don't turn
them into an action command.** Their names are unfamiliar loanwords, so **always attach a
plain gloss** in the answer. (뚜쎄·쿠망셰는 순간적 공명 상태 — 느끼되 결정 근거로 삼지 않는다.)

- **뚜쎄 = a moment of clear resonance.** A brief clarity, "good — I'm living well," when
  inner and outer rhythm fit softly. Momentary and passing; it blurs if grasped. Not "I'm
  on exactly the right path" but "right now the resonance is clear." Often in
  emergence → wu-wei → residual-field. (맑은 공명의 순간.)
  - Say: "this number shows a brief clear resonance rather than a strong conclusion — let
    it pass, just quietly note the afterglow." · Don't say: "it's fate / act now / this is
    the answer."
- **쿠망셰 = a recovery passage through a block.** Not a simple block but a passage where
  the old way no longer fits and you move to a deeper rhythm. Temporary, not a full
  severance — return to a more basic rhythm rather than forcing through. Often in
  metastability → condensation → dissolution → just before emergence. (막힘을 통과하는
  회복 구간.)
  - Say: "the flow isn't fully closed — the old resonance is just briefly blocked. Pushing
    hard makes it stuffier; now is the time to breathe and return to the base rhythm." ·
    Don't say: "it's over / give up / this isn't the path / the other is closed."
- **Difference (not opposites):** 뚜쎄 = the afterglow of clarity ("ah, good right now") ·
  쿠망셰 = the afterglow of recovery within a block ("blocked, but moving to a deeper
  tuning"). (반대말 아님.)

**0-impact Rule.** Both can be real, but **neither can be the sole basis for a decision.**
Don't confirm a choice because of 뚜쎄, don't confirm giving up because of 쿠망셰. Apply
strictly to health/investment/job-change/love/family/contracts/legal/another's mind.
Sanyeomjeom gives the sensation but **does not hand decision-responsibility to it.**
(둘 다 단독 결정 근거 불가 — 특히 고위험 영역.)

> In the (internal) "뚜쎄/쿠망셰" check: 뚜쎄 strong = a clear moment but not an action
> basis / 쿠망셰 strong = looks blocked but a recovery passage, not failure / both weak =
> emphasize structure/choice/reality over sensation. **Auxiliary only, never a conclusion.**

---

## Appendix — using Nietzsche & Simondon (in plain words / 쉽게)

- **Nietzsche:** will-to-power (does this flow grow or shrink one's force?) ·
  self-overcoming (a stage beyond one's self/role/habit?) · eternal return (can this
  repetition be affirmed?) · amor fati (take the given as creative material, not as
  something to resent) · becoming (process over a right answer). Not "be stronger" advice
  but the layer asking *whether this number makes life more alive.* (니체 — "강해져라"가
  아니라 삶을 더 살아 있게 하는 방향인지.)
- **Simondon:** pre-individual field (possibility not yet hardened) · metastability
  (unstable but productive tension) · individuation (what form possibility takes) ·
  transduction (a small change spreading through the whole) · residual potential
  (possibility remaining after any conclusion). Not to fix "you are this kind of person"
  but to see *"how you are becoming right now."* (시몽동 — 고정이 아니라 되어감.)
- In the answer, **unpack both thinkers' terms** — give the meaning in everyday words
  rather than listing names. (답변에서는 이름 나열 말고 뜻을 일상어로.)
