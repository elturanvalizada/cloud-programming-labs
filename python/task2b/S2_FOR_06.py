# S2_FOR_06 — Sum nested lists (matrix)

def sum_nested(matrix):
    total = 0

    for row in matrix:
        if not isinstance(row, list):
            return None
        for value in row:
            total += value

    return total


def main():
    tests = [
        [[1, 2], [3, 4]],          # 10
        [[-1, 2, 3], [4]],         # 8
        [[]],                      # 0
        [],                        # 0
        [[1, 2], "not a list"],    # None
    ]

    for t in tests:
        print(f"matrix={t} -> sum={sum_nested(t)}")


if __name__ == "__main__":
    main()
