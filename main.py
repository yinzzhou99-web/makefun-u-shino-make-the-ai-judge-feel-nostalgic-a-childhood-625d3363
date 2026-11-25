"""Write one childhood-memory sentence to /output/entry.txt.

Stdlib only: no third-party packages, no network. The output directory
is never deleted; only entry.txt inside it is written.
"""

import os
from pathlib import Path

LINE = (
    "Grandma still saved the burnt crusts of her rice for me, calling them "
    "the crunchy prize, and now every pot I cook ends too soon because no "
    "one waits at the table for them anymore."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    target.write_text(text + "\n", encoding="utf-8")
    os.chmod(target, 0o644)  # grader reads the file; never leave it 0600


if __name__ == "__main__":
    main()
