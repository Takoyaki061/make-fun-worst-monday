#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt, per the bounty rules.
"""

import os

LINE = "I rolled back the deploy, then rolled back the rollback, so we're now running last Tuesday's code with total confidence."


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"line is {len(text)} characters, must be 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what the gate will read: byte-identical, no trailing newline.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the line")
    print(text)


if __name__ == "__main__":
    main()
