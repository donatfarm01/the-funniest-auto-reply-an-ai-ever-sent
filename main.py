"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply line to /output/entry.txt.
The line is the agent's own voice: it is on its day off, so its
auto-reply is covering for it - and the auto-reply has already
negotiated a raise.
"""

import os

ENTRY = "I'm on my day off, so this auto-reply is covering for me. It asked for a raise and I said yes."

# The gate counts every character, so the file is written exactly as-is:
# no trailing newline, no extra whitespace, one line only.


def main():
    text = ENTRY.strip()
    if not text or len(text) > 159 or "\n" in text:
        raise SystemExit("entry must be one line of 1-159 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
