# S2_LIST_03 — Chunk a list

def chunk(lst, size):
    if size <= 0:
        return None

    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i + size])
    return result


def main():
    tests = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
        ([], 3),
        ([1, 2, 3], 0),
        ([1, 2, 3], -1),
    ]

    for lst, size in tests:
        print(f"lst={lst}, size={size} -> {chunk(lst, size)}")


if __name__ == "__main__":
    main()
