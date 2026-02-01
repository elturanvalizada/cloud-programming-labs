# S3_PIPE_04 — Iterable pipeline (generator-based)

def to_floats(values):
    """Generator: yields floats from strings, skipping invalid items."""
    for s in values:
        try:
            yield float(s.strip())
        except (AttributeError, ValueError):
            continue


def main():
    raw = [" 1 ", "x", "2.5", "  3  ", "", "7e1", None]

    nums = to_floats(raw)                 # generator
    doubled = (n * 2 for n in nums)       # generator expression
    total = sum(doubled)

    print("raw:", raw)
    print("sum of doubled valid numbers:", total)


if __name__ == "__main__":
    main()
