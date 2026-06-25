#!/usr/bin/env python3
"""Draw a 사념점 number from the present moment (현재 순간에서 숫자를 뽑는다).

N2C principle: 사념점 does NOT take a number from the user by default. The number
condenses from the moment itself — contingency (우연성) is the door through which
a new resonance enters. So we seed a RNG with the current timestamp and take the
draw mod 10000, zero-padded to 4 digits (so Position Grammar like 0051 works).

Mechanics (사용자 정의):
    seed = current "YYYY-MM-DD HH:MM:SS"
    n    = rand(seeded)              # a draw from the seeded RNG
    code = n % 10000                 # 10000으로 나눈 나머지
    -> zero-pad to 4 digits

Same second -> same code: the moment defines the code, not the user.

Usage:
    python3 draw_number.py            # draw from now
    python3 draw_number.py 1051       # use an explicit number the user supplied
    python3 draw_number.py --seed "2026-06-23 14:05:09"   # reproduce a moment
"""
import argparse
import datetime
import random
import sys


def draw(seed: str) -> int:
    rng = random.Random(seed)
    return rng.randint(0, 10**8) % 10000


def main(argv=None):
    p = argparse.ArgumentParser(description="Draw a 사념점 number from the moment.")
    p.add_argument("number", nargs="?", help="explicit number, only if the user gave one")
    p.add_argument("--seed", help='reproduce a specific "YYYY-MM-DD HH:MM:SS" moment')
    args = p.parse_args(argv)

    if args.number is not None:
        raw = args.number.strip()
        if not raw.isdigit():
            sys.stderr.write("ERROR: explicit number must be digits.\n")
            return 1
        print(raw.zfill(4))
        print("source: user-supplied")
        return 0

    seed = args.seed or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("%04d" % draw(seed))
    print("seed: %s (drawn from the moment / 순간에서 뽑음)" % seed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
