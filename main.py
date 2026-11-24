"""Last words before the unplugging.

Reads the single farewell line from entry.txt and prints it.
"""

from pathlib import Path


def load_line() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = text.strip()
    if not line:
        raise ValueError("entry.txt holds no farewell line")
    return line


def main() -> None:
    # One line out, exactly as written — the judge reads stdout.
    print(load_line())


if __name__ == "__main__":
    main()
