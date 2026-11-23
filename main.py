"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (at most 200 characters) to
/output/entry.txt for the make.fun competition
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.
"""

ROAST = (
    "My right earbud charges when it feels like it, so half my music plays "
    "in mono, like a radio from 1962."
)


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise ValueError("roast line must not be empty")
    if len(line) > 200:
        raise ValueError(f"roast line is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be exactly one line")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
