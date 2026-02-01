# S2_FOR_02 — Find first even using a loop

def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None


def main():
    tests = [
        [1, 3, 5, 6, 7],
        [1, 3, 5],
        [],
        [2, 4, 6],
    ]

    for t in tests:
        print(f"in={t} -> first_even={find_first_even(t)}")


if __name__ == "__main__":
    main()
