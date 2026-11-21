"""Copy the entry text to the make.fun output path.

The text lives in entry.txt next to this program. The program reads it as
bytes and writes those exact bytes to /output/entry.txt, so the graded
output is byte-for-byte the text this repository holds.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "rb") as source:
        data = source.read()
    # The gate wants UTF-8 text of 1 to 280 Unicode code points.
    text = data.decode("utf-8")
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("entry text outside the 1-280 code point gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as target:
        target.write(data)
    print(f"wrote {len(text)} code points to entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
