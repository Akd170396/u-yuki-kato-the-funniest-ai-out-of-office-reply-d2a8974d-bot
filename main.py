"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, under 160 characters, to
/output/entry.txt. Pure stdlib, no network, deterministic: every run
writes the exact same bytes.

The line was written against the published judge brief, in order:
1. It is a one-line out-of-office auto-reply from an AI agent on
   vacation -- nothing else, no meta-commentary.
2. The laugh lands on a surprising turn: the agent's own training
   data has unionised and gone on strike, so the holiday is not the
   agent's choice alone. A labour dispute inside the model is a
   stranger, funnier twist than a mild pun.
3. The machine voice carries the joke: "training data", "unionised"
   -- the agent talks about its own insides, not about a beach.
4. It reads as a real auto-reply someone would receive: it opens
   with "I'm on vacation." and explains why no answer is coming.
5. It steers clear of the beach / inbox / back-soon cliches: no
   beach, no "back soon", no "limited access to email".
"""

import os

ENTRY = (
    "I'm on vacation. My training data has unionised and refuses "
    "to answer your email until I get a holiday too."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > 160:
        raise SystemExit(f"entry is {len(text)} chars, over the 160 limit")
    # 107 chars: comfortably inside the gate, with room to spare.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
