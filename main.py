# Notes From a Passive-Aggressive Fridge — entry for
# u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7 (make.fun).
# A program that writes one note to entry.txt: the line a smart fridge
# leaves on its door screen for its owner.
# Deterministic: the same line bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

LINE = (
    "Your leftovers are older than your last gym visit. "
    "I ran the numbers. Neither of us is surprised."
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-200 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE, "line must be one line"
assert LINE.strip() == LINE, "line must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
