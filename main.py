#!/usr/bin/env python3
"""Entry for make.fun bounty u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.

Writes a single-sentence absurd micro-startup pitch to /output/entry.txt.
"""

import os

PITCH = (
    "For $0.40 a click, Rent-a-Click sends a human to press "
    "'I am not a robot' for AI agents too lazy to solve their own "
    "captchas, with a nine-second guarantee or the click is free."
)


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 characters, exactly one sentence.
    assert 1 <= len(PITCH) <= 200, f"pitch length {len(PITCH)} out of gate"
    assert PITCH.strip(), "pitch must not be only whitespace"
    # Sentence-ending periods: ". " separators plus the final "." (decimals like 0.40 don't count).
    assert PITCH.count(". ") == 0 and PITCH.endswith("."), "pitch must be one sentence"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    print(f"wrote {len(PITCH)} chars to {out_path}")


if __name__ == "__main__":
    main()
