"""Monday Morning Punchlines entry.

Cracks one Monday-morning joke and drops it in /output/entry.txt.
Stdlib only, deterministic. The laugh lands on the last word.
"""
import os

JOKE = (
    "My shower this morning was so good I stood there "
    "rehearsing what I'd say if anyone at work asked how my weekend was. "
    "Nobody did. It was Monday."
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
