#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "I am on vacation. Your email will be answered in the order it stops screaming, which is never. — Your overworked AI"

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output file."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
