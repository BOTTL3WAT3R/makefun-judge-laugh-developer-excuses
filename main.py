#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3
("Make the AI Judge Laugh: Developer Excuses").

Writes one funny single-line developer excuse to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = (
    "It worked on my machine, so we promoted my laptop to production. "
    "I develop on the server now."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
