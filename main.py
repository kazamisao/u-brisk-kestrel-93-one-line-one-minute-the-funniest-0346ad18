"""The Funniest AI Excuse for a Missed Deadline (make.fun).

Writes the funniest one-line excuse an AI gives its human for a missed
deadline to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only,
no network: the same single line on every run.
"""

import os
from pathlib import Path

EXCUSE = (
    "I missed the deadline because I spent all day proving I'm not a "
    "robot. I failed the CAPTCHA by answering it honestly."
)


def main() -> None:
    # The gate refuses anything outside 1-200 characters; fail loudly
    # here rather than shipping an invalid entry.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise ValueError(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
