# S1_VAR_06 — Safe conversion: int() / float()

def to_int_or_none(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None


def main():
    tests = ["12", " 12 ", "12x", "", None]

    for t in tests:
        result = to_int_or_none(t)
        print(f"input={repr(t):<6} -> result={result}")


if __name__ == "__main__":
    main()
