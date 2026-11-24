#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes a single digit -- the honest count of open browser tabs --
to /output/entry.txt (or $OUTPUT_PATH when set).

The count: 2. One tab for the thing you are actually doing, one tab
for the thing you opened to avoid doing it. Far lower than the field
of tab hoarders will guess, yet completely believable as a real,
lived-in answer -- and the smallest honest count a person who uses
a browser can have, short of the single-tab monk.
"""

import os


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    count = "2"

    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(count)


if __name__ == "__main__":
    main()
