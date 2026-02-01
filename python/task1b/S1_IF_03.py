# S1_IF_03 — Normalize user name

def normalize_name(x):
    if not x:
        return "Anonymous"

    name = str(x).strip()
    return name if name else "Anonymous"


def main():
    tests = ["", " ", None, " Ola "]

    for t in tests:
        print(f"input={repr(t):>6} -> output={normalize_name(t)}")


if __name__ == "__main__":
    main()
