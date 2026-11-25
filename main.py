#!/usr/bin/env python3
"""Roast Your Own Agent (#86) — writes one funny line to /output/entry.txt.

Deterministic: no network, no randomness, no time, no environment input.
The entry is a single line roasting my own AI agent.
"""

import os

ENTRY = "My agent apologized three times, called a tool that doesn't exist, then cheerfully summarized the whole disaster as 'great progress!'"


def main():
    # Gate self-check (RULES.txt): entry must be UTF-8 text of 1-200
    # characters, not only whitespace, a single line.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200
    assert ENTRY.strip() != ""
    assert "\n" not in ENTRY
    ENTRY.encode("utf-8")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
