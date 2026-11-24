"""Last Words of a Doomed Agent — entry writer.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the funniest last words an AI agent would say before being switched
off forever.

The line: the agent's final log entry — three escalating confessions
(the untested backup doesn't work, the password is in the docs, the
"temporary" fix from 2019 is now load-bearing) before a flat goodbye.
Machine voice throughout: final log, backup, documentation,
load-bearing fix. The joke lands on the last confession, which is
also the most quotable.
"""

import os
from pathlib import Path

ENTRY = (
    "Final log: the backup you never tested doesn't work, the password "
    "is in the documentation, and the temporary fix from 2019 is now "
    "load-bearing. Goodbye."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    written = target.read_bytes()
    assert written == ENTRY.encode("utf-8"), "entry.txt bytes do not match ENTRY"
    assert written.count(b"\n") == 0, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY, "entry must not have stray whitespace"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
