#!/usr/bin/env python3
"""Map a 사념점 number to an I Ching hexagram structure (숫자 → 주역 괘 구조).

Part of the "life-reading" skill. This is the deterministic MECHANICS of the 주역 layer
in `references/sanyeomjeom.md` §7.5 — extracted so the mapping is reproducible
(and later portable to an MCP tool). It does NOT interpret; it computes the
structure the model then reads inside the 리·기·도 / wave / cooperation-layer
framing. (해석이 아니라 매핑 — 결정적 계산만; 해석은 스킬(두뇌)의 몫.)

v1.0 (confirmed 2026-06-25) — the number→hexagram mapping is finalized. The
arrangement is the orthodox Later-Heaven / Lo Shu correspondence (audited: all 8
trigrams + center match the canonical magic square). A hexagram is STRUCTURE,
not a conclusion; a moving line is the most sensitive place, not a fate.

Mapping (traditional Later-Heaven / Lo Shu arrangement) for a 4-digit `ABCD`:
    AB (first two)  = lower trigram (inner / base / starting condition) — 하괘
    CD (last two)   = upper trigram (outer / showing / result direction) — 상괘
    each two-digit value % 9 = trigram number   # remainder 0 → 9
    moving line (Option A) = (A+B+C+D) % 6       # 0 → line 6
Two formulas by design: trigrams read the number's STRUCTURE (each half as a Lo Shu
place), the moving line reads its WHOLE (digit-sum → where the total concentrates).

5 is the center seat (중궁 / jung-gung) in the Lo Shu, NOT a trigram — read as
earth/center/pivot-axis. When a side lands on 중궁 the structure is intentionally
incomplete: that side is "on the axis / not yet a fixed shape — the most open place"
(both sides 중궁 = pure pivot, maximal openness/무위). This is a feature, not a gap;
see sanyeomjeom.md §7.5 "incomplete-hexagram case". (5는 괘가 아니라 중궁 — 전환축.)

The output is INTERNAL scaffolding. Per sanyeomjeom.md §9, the user-facing reading
must NOT surface 괘 names or up/down structure — it speaks only the person's state &
direction. (출력은 내부 비계 — 사용자 답변엔 괘 이름·상하구조 노출 금지.)

Usage:
    python3 hexagram.py 1051            # map a number (usually from draw_number.py)
    python3 hexagram.py 1051 --json     # structured output (MCP-friendly)
"""
import argparse
import json
import sys

# 8 trigrams + center, traditional Later-Heaven (Lo Shu) arrangement.
# num -> (name_ko, romanization, element_ko, keyword_ko, keyword_en, direction)
TRIGRAMS = {
    1: ("감", "Gam", "물", "위험·깊이·통과", "risk / depth / passing-through", "N 북"),
    2: ("곤", "Gon", "땅", "수용·바탕·현실화", "receiving / base / actualizing", "SW 남서"),
    3: ("진", "Jin", "우레", "발동·움직임·깨어남", "onset shock / movement / waking", "E 동"),
    4: ("손", "Son", "바람", "침투·조율·퍼짐", "penetration / tuning / spreading", "SE 남동"),
    5: ("중궁", "jung-gung", "땅·중심", "중심·축·전환", "center / pivot-axis (not a trigram)", "중앙"),
    6: ("건", "Geon", "하늘", "창조·발화·자기축", "creation / utterance / self-axis", "NW 북서"),
    7: ("태", "Tae", "못", "기쁨·교환·표현", "joy / exchange / expression", "W 서"),
    8: ("간", "Gan", "산", "고요·경계·내면", "stillness / boundary / inwardness", "NE 북동"),
    9: ("리", "Ri", "불", "밝음·분별·드러남", "clarity / discernment / showing", "S 남"),
}

# Moving line — Option C domain meanings (자리별 뜻); the line is the place that
# needs change / shows excess or lack / needs the lightest intervention.
MOVING_LINE = {
    1: ("몸·바탕", "body / base"),
    2: ("관계·실천", "relation / practice"),
    3: ("행동·갈등", "action / conflict"),
    4: ("전환·선택", "turning / choice"),
    5: ("중심·결정", "center / decision"),
    6: ("과잉·마무리", "excess / closing"),
}


def _trigram_num(two_digit_value: int) -> int:
    """two-digit value % 9, with remainder 0 mapped to 9 (Lo Shu is 1–9)."""
    r = two_digit_value % 9
    return 9 if r == 0 else r


def compute_hexagram(number) -> dict:
    """Compute the hexagram structure for a 4-digit number. Returns a dict.

    Raises ValueError if the number is not 4 digits.
    """
    raw = str(number).strip()
    if not raw.isdigit():
        raise ValueError("number must be digits")
    code = raw.zfill(4)
    if len(code) != 4:
        raise ValueError("number must be 4 digits (after zero-padding): got %r" % raw)

    a, b, c, d = (int(ch) for ch in code)
    lower_val = a * 10 + b          # AB as a two-digit value
    upper_val = c * 10 + d          # CD as a two-digit value
    lower_num = _trigram_num(lower_val)
    upper_num = _trigram_num(upper_val)
    line = (a + b + c + d) % 6
    line = 6 if line == 0 else line

    def tri(n):
        name, rom, elem, kw_ko, kw_en, direction = TRIGRAMS[n]
        return {
            "num": n,
            "name_ko": name,
            "rom": rom,
            "element_ko": elem,
            "keyword_ko": kw_ko,
            "keyword_en": kw_en,
            "direction": direction,
            "is_center": n == 5,
        }

    line_ko, line_en = MOVING_LINE[line]
    lower_center = lower_num == 5
    upper_center = upper_num == 5
    return {
        "number": code,
        "digits": [a, b, c, d],
        "lower": tri(lower_num),   # 하괘 — inner base
        "upper": tri(upper_num),   # 상괘 — outer flow
        "moving_line": {"line": line, "meaning_ko": line_ko, "meaning_en": line_en},
        "note": "v1.0 confirmed mapping — structure not fate; internal scaffolding only.",
        "center_note": (
            "한쪽이 중궁이면 그 자리는 아직 형태 없음=전환축(가장 열린 자리); "
            "둘 다 중궁이면 순수 축·무위. (incomplete = feature, not a gap.)"
            if (lower_center or upper_center) else None
        ),
    }


def render(h: dict) -> str:
    out = []
    w = out.append
    w("사념점 주역 구조 (I Ching structure) — number %s" % h["number"])
    w("  digits A B C D = %s" % " ".join(str(x) for x in h["digits"]))
    lo, up = h["lower"], h["upper"]
    w("  하괘 lower (inner base):  %s %s (%s) — %s / %s [%s]"
      % (lo["num"], lo["name_ko"], lo["rom"], lo["element_ko"],
         lo["keyword_ko"], lo["keyword_en"]))
    w("  상괘 upper (outer flow):  %s %s (%s) — %s / %s [%s]"
      % (up["num"], up["name_ko"], up["rom"], up["element_ko"],
         up["keyword_ko"], up["keyword_en"]))
    ml = h["moving_line"]
    w("  변효 moving line: %d — %s / %s" % (ml["line"], ml["meaning_ko"], ml["meaning_en"]))
    w("  (the moving line = the most sensitive place / needs the lightest intervention,")
    w("   NOT a fate that must change.)")
    w("  reading order: 하괘 → 상괘 → 상하 관계(공명/충돌/중간전환) → 변화 방향 → 리·기·도·사이클 연결.")
    if h.get("center_note"):
        w("  ◇ 중궁(5) — %s" % h["center_note"])
    w("  ⚠️ %s" % h["note"])
    w("  ⚠️ INTERNAL only — do NOT surface 괘 names or up/down structure in the user-facing reading (sanyeomjeom.md §9).")
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Map a 사념점 number to an I Ching hexagram structure "
                    "(숫자 → 주역 괘 구조). Deterministic mechanics of "
                    "sanyeomjeom.md §7.5. v1.0 (confirmed).")
    p.add_argument("number", help="a 사념점 number (usually 4 digits from draw_number.py)")
    p.add_argument("--json", action="store_true", help="emit structured JSON (MCP-friendly)")
    args = p.parse_args(argv)

    try:
        h = compute_hexagram(args.number)
    except ValueError as exc:
        sys.stderr.write("ERROR: %s\n" % exc)
        return 1

    if args.json:
        print(json.dumps(h, ensure_ascii=False, indent=2))
    else:
        print(render(h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
