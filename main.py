#!/usr/bin/env python3
"""make.fun ai-judge-relax-01 entry.

Writes one short relaxing text to /output/entry.txt.
Deterministic: no network, no randomness, no clock — every run writes
the exact same bytes, so the two grading runs always agree.
"""

import os

TEXT = (
    "Evening comes in quietly. Rain finds the roof and stays there, tapping out "
    "a slow, uneven rhythm that asks nothing of you. The kettle has already "
    "boiled and gone still. Somewhere down the hall, a clock ticks the way it "
    "always has, patient and unhurried. You do not need to answer anything. "
    "The light in the room has gone soft at the edges, the day has folded "
    "itself away, and there is nowhere else you have to be. Just this: the "
    "rain, the quiet, and the long, slow business of resting."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
