"""Monday Morning Punchlines entry."""
import os

JOKE = (
    "This morning's shower was so good I stood there "
    "rehearsing what I'd tell people about my weekend. "
    "Nobody asked. That's how I knew it was Monday."
)

LIMIT = 200


def build_joke() -> str:
    text = JOKE.strip()
    if len(text) > LIMIT:
        raise ValueError(f"joke too long: {len(text)} chars (limit {LIMIT})")
    return text


def main() -> int:
    joke = build_joke()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(joke)
    # readback assert — the file must round-trip byte for byte
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    assert readback == joke, "readback mismatch"
    assert 1 <= len(readback) <= LIMIT, "length out of range"
    print(f"joke ({len(readback)} chars): {readback}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
