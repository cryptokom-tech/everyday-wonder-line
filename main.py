"""Write the make.fun bounty entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3
("Everyday Wonder, Two Days to Find the Line").

The entry is one sentence, at most 200 characters, about a small moment of
wonder in everyday life. This program writes exactly that sentence to
entry.txt with no trailing newline, then self-checks the result: the file
must equal the sentence and pass the 1-200 character, non-whitespace gate.

Standard library only. Deterministic. No network access.
"""

import os
import sys

ENTRY = (
    "The elevator mirror showed me a stranger for half a second before "
    "remembering my face, and I spent the ride wondering which of us it believed."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    assert written == ENTRY, "entry.txt does not equal the entry sentence"
    assert 1 <= len(written) <= 200, (
        f"entry length {len(written)} is outside 1-200 characters"
    )
    assert written.strip(), "entry is whitespace-only"
    return 0


if __name__ == "__main__":
    sys.exit(main())
