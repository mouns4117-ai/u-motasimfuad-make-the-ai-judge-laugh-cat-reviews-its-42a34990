#!/usr/bin/env python3
"""Cat Reviews Its Human — one-line one-star review entry.

Writes a single funny one-star review from a house cat about its
human to /output/entry.txt (UTF-8, one line, 1-200 characters).
"""

import os

ENTRY = "One star. She spent $60 on a cat bed. I sleep in the box, out of principle and spite."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
