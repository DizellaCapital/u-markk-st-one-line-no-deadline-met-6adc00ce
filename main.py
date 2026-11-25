"""One Line, No Deadline Met — single-line excuse for a missed deadline.

The entry is one sentence: a specific moment (11:58), a concrete
artifact (the office Wi-Fi dying at 99% and the file timestamp), and
a turn at the end — the timestamp itself writes the excuse. It reads
like something a person would actually say when cornered, not a
generic apology and not a personified deadline.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Python standard library only.
"""

import os
import sys

LINE = (
    "I uploaded it at 11:58, the office Wi-Fi cut out at 99%, and by "
    "the time it reconnected the timestamp had already written my "
    "excuse for me in a font I can't argue with."
)

# Gate from the bounty rules: the sealed scorer only accepts 1-200
# characters, and the judge brief wants a single sentence with the
# punch at the end. Keep the entry inside 1-199 so the trailing
# newline the file write adds never pushes it over the gate.
MAX_CHARS = 199


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    if LINE.count("\n") or LINE.count(".") != 1:
        raise ValueError("entry must be a single sentence on one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
