#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt (make.fun program/v1).

The line: one excuse a gamer texts the boss to skip work on GTA 6
launch week, at most 20 words. Chosen against the judge brief
(RULES.txt): a real, specific, boring building detail (water cut 9-5,
plumber needs access to the flat) a tired manager would almost
believe; the humour comes from the bureaucratic helplessness itself,
not a bolted-on joke; reads like a text sent in a hurry, ending in a
bare "sorry". Council consultation approved this line as-is, and an
independent reviewer approved it as-is too (both recorded in the
consultation log). The program self-checks the gate before writing,
so a future edit that broke the 1-140 character / 20-word / one-line
limits would fail loudly here instead of silently shipping an
invalid entry.
"""
import os

LINE = "Building cut our water 9-5 for pipe repairs, plumber needs access to my flat, sorry"

# The gate (RULES.txt): UTF-8 text of 1 to 140 characters, not only
# white space; the task adds one line of at most 20 words.
assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert LINE.strip() != "", "line must not be only white space"
assert "\n" not in LINE, "line must be a single line"
assert len(LINE.split()) <= 20, "line must be at most 20 words"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
