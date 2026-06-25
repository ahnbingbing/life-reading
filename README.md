# life-reading (n2c) — Neo²-Confucianism / Dynamic Resonance Ontology

> **life-reading** is the skill; **N2C (n2c)** — Neo²-Confucianism / Dynamic Resonance
> Ontology — is the philosophy it reads through. (스킬 이름은 life-reading, 그 바탕
> 철학이 N2C·리·기·도.)

An installable Claude skill that interprets phenomena — situations, texts,
emotions, dreams, conversations, images, and numbers (사념점) — through **N2C**, a
philosophy that reads existence as a **dynamic resonance trajectory** formed by
리(Li, latent structure), 기(Gi, active flow), 도(Do, footprint), 파동(wave), and a
공조층(cooperation layer).

> **This is not fortune-telling.** N2C is **not** fatalism, MBTI, tarot, or
> astrology. It offers *local inference* on a resonance trajectory and **returns
> the final choice to you** — it never declares a fixed future. "Already-there is
> not already-decided." (운명론·점·MBTI·타로·점성술이 아니다. 고정된 미래를
> 단정하지 않고, 공명 궤적에 대한 국소 추론을 주며 최종 선택은 사용자에게 돌려준다.)

## What it does

Four things, all as *local inference* that returns the choice to you:

- **Read any input through N2C** — a situation, text, emotion, dream, or symbol:
  identify 리 / 기 / 도, read wave and the cooperation layer, locate the phase of the
  cycle (응축 → 해산 → 창발 → 무위), and offer a minimal-interference (무위) move.
- **사념점 (Sanyeomjeom) number readings** — the number is **drawn from the present
  moment** (timestamp seed → mod 10000 → 4 digits via `scripts/draw_number.py`),
  not taken from user input, then read as an independent resonant code (Number /
  Position / Pattern grammar, the 리·기·도 + wave + cooperation layers, plain-language
  emotional signals, an extended N2C × Nietzsche × Simondon cycle, an auxiliary
  뚜쎄/쿠망셰 read at 0-impact, an internal I Ching structure layer, and domain lenses).
- **A vs B recommendation** — reads which way the moment's tilt leans and recommends
  accordingly. Not forced to A/B: the answer may be A, B, both, neither ("leave a gap"),
  or stay-as-is — whichever the reading points to. A lean, not a verdict.
- **Life-reflection / counseling** — working through a hard time, a recurring
  relationship pattern, or "where is this heading?" in a dry-but-kind register. With
  care: pure venting → listen first; crisis/safety → no reading, direct to real help.

## Quickstart

Once installed, just ask in natural language (English or Korean):

- `사념점 한번 봐줘` — a number reading drawn from this moment
- `맥북 프로랑 에어 중에 뭐가 나을까?` — an A vs B lean
- `요즘 같은 일이 자꾸 반복돼. 이걸 어떻게 봐야 할까?` — a situation / pattern reading
- `Read this moment through 리·기·도` — a philosophical resonance read

The answer follows the language you ask in. The number's mechanics (digit values,
I Ching 괘) stay internal — you see only your state and direction, in plain words.

## Example reading

> **You:** 요즘 일이 손에 잘 안 잡히고, 이대로 가는 게 맞나 자꾸 다른 길이 있나 싶어.
> 마음이 붕 떠 있는 느낌이야. 사념점 한번 봐줄래?
>
> **life-reading** *(number 9421, drawn from the moment):* …지금 너 안에서 하나의
> 사이클이 끝나가는 중이야. 한참 붙들고 있던 게 다 여물어서, 오히려 풀리고 흩어지는
> 국면. … **지금 할 일 (한 수):** 큰 결정은 한 박자 미루고, "지금 붙들고 있는 것들" 중
> 이미 끝난 것 하나를 골라 오늘 깔끔하게 닫아. 그 자리가 비어야 다음 방향이 들어와. …
> 방향은 네가 이미 알고 있어 — 고를 키는 네 손에 있어.

Full reading in [`README.ko.md`](README.ko.md#예시-사념점-리딩).
점이 아니라 읽기다 — it never declares a fixed future.

## Scope

v0.1 = the philosophy core (ontology, principles, ethics, the cycle) **plus the
full 사념점 reading method.** This skill stays true to the philosophy; the
data-driven PM/operations application of N2C lives in the separate
**`aligned-delivery`** skill. The two share the 리·기·도 root and **compose**: N2C
may accompany a PM decision as an auxiliary, 0-impact resonance lens, but a plain
PM request routes to `aligned-delivery` and its data drives the decision.

## Files

```
life-reading/
├── SKILL.md                    # entry point: 12 core principles + 10 interpretation rules + Do-Not
├── README.md / README.ko.md
├── CHANGELOG.md                # 0.1.0
├── LICENSE                     # MIT © 2026 Yuri Ahn
├── .gitignore
├── references/
│   ├── ontology.md             # 리·기·도, wave, cooperation layer, contingency, spiral, cycle
│   ├── sanyeomjeom.md          # the full 사념점 method (v0.1)
│   └── n2c-source.md           # the author's original source, preserved verbatim
├── scripts/
│   ├── draw_number.py          # draw the 사념점 number from the present moment (timestamp seed)
│   └── hexagram.py             # map a number → I Ching hexagram structure (sanyeomjeom §7.5, v1.0)
└── evals/
    └── evals.json
```

## Install

Copy the `life-reading/` directory into `~/.claude/skills/` (or your project's
`.claude/skills/`). The skill activates when you ask for an N2C reading or a
사념점.

## License

MIT © 2026 Yuri Ahn. (A philosophical/prose work — switch to CC BY 4.0 if you
prefer; see LICENSE.)
