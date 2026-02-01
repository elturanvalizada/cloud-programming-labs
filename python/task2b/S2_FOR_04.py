# S2_FOR_04 — Count occurrences (histogram)

def count_occurrences(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts


def main():
    tests = [
        [1, 2, 2, 3, 1, 2],
        ["a", "b", "a", "c", "b", "a"],
        [],
        [True, False, True, True],
    ]

    for t in tests:
        print(f"in={t} -> counts={count_occurrences(t)}")


if __name__ == "__main__":
    main()
