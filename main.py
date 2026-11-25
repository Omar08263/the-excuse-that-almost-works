#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt (make.fun program/v1).

The line: one excuse a gamer texts the boss to skip work on GTA 6
launch week, at most 20 words. Chosen against the judge brief
(RULES.txt): a real, specific, boring building detail (water cut 9-5,
plumber needs access to the flat) a tired manager would almost
believe; the humour comes from the bureaucratic helplessness itself,
not a bolted-on joke; reads like a text sent in a hurry, ending in a
bare "sorry". Council consultation approved this line as-is.
"""
import os

LINE = "Building cut our water 9-5 for pipe repairs, plumber needs access to my flat, sorry"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
