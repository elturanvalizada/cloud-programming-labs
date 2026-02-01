# S2_FOR_03 — Sum until threshold

def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total


def main():
    tests = [
        ([1, 2, 3, 4], 5),     # 1+2=3, next 3 would exceed -> 3
        ([5, 5, 5], 10),       # 5+5=10
        ([1, 2, 3], 100),      # sum all
        ([10, 1], 5),          # first already exceeds -> 0
        ([], 10),
    ]

    for nums, t in tests:
        print(f"nums={nums}, threshold={t} -> sum={sum_until(nums, t)}")


if __name__ == "__main__":
    main()
