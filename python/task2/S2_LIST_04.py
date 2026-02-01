# S2_LIST_04 — Flatten one level

def flatten1(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                result.append(x)
        else:
            result.append(item)
    return result


def main():
    tests = [
        [1, [2, 3], [4], 5],
        [[1, 2], [3, 4]],
        [1, 2, 3],
        [],
        [[1, [2, 3]], 4],  # only one level flattened
    ]

    for t in tests:
        print(f"in={t} -> out={flatten1(t)}")


if __name__ == "__main__":
    main()
