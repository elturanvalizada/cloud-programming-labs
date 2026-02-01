# S2_LIST_02 — Deduplicate without set

def unique(values):
    result = []
    for v in values:
        if v not in result:
            result.append(v)
    return result


def main():
    tests = [
        [1, 2, 2, 3, 1],
        ["a", "b", "a", "c", "b"],
        [],
        [True, True, False, True],
    ]

    for t in tests:
        print(f"in={t} -> out={unique(t)}")


if __name__ == "__main__":
    main()
