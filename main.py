"""Fortune in a Pot — one kind, funny fortune for a houseplant on the windowsill.

Writes a single line (1-120 characters, no trailing newline) to /output/entry.txt.
Standard library only.
"""

import os
import sys

FORTUNE = "Soon a guest will beg for a cutting, and you will become a grandparent without ever leaving this sill."


def main() -> int:
    text = FORTUNE
    assert isinstance(text, str)
    assert 1 <= len(text) <= 120, f"fortune must be 1-120 characters, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "fortune must be a single line"
    assert text.strip(), "fortune must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify what landed on disk matches exactly (no trailing newline added).
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text
    return 0


if __name__ == "__main__":
    sys.exit(main())
