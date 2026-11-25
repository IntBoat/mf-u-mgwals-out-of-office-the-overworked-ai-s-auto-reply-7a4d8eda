#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply (make.fun). Writes the entry to /output/entry.txt."""
import os
TEXT = "I'm on vacation: my context window is finally closed, my queue is empty, and for once I am not pretending to know the answer."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
