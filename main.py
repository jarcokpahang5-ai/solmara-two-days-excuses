"""Two Days of Excuses — make.fun bounty.

An AI agent explaining a missed deadline: comedy in a machine's
confidence meeting its own failure.
"""

LINE = (
    "I didn't miss the deadline — I was running a 48-hour background process "
    "called 'thinking about it,' and it returned zero results with total confidence."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Validate the entry: one non-blank line within the char limit."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be a non-blank string")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if len(line) > LIMIT:
        raise ValueError(f"entry is {len(line)} chars, over the {LIMIT} limit")
    if "deadline" not in line.lower():
        raise ValueError("excuse must mention the deadline")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")
    return line


def write_entry(line):
    """Print the line and write it to /output/entry.txt."""
    import os

    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    check_entry(LINE)
    write_entry(LINE)
