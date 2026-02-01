# S2_LIST_01 — Clean number strings

def clean_numbers(values):
    result = []
    for s in values:
        try:
            n = float(s.strip())
            result.append(n)
        except (AttributeError, ValueError):
            # AttributeError: s is not a string-like object with .strip()
            # ValueError: float conversion failed
            continue
    return result


def main():
    tests = [
        [" 1 ", "x", "2"],
        ["3.5", "  4  ", "bad", "0"],
        ["", "   ", "7"],
        [],
    ]

    for t in tests:
        print(f"in={t} -> out={clean_numbers(t)}")


if __name__ == "__main__":
    main()
