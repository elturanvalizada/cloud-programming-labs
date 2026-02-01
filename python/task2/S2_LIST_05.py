# S2_LIST_05 — Stats

def stats(nums):
    if not nums:
        return None

    total = 0
    min_v = nums[0]
    max_v = nums[0]

    for n in nums:
        total += n
        if n < min_v:
            min_v = n
        if n > max_v:
            max_v = n

    avg = total / len(nums)

    return {
        "min": min_v,
        "max": max_v,
        "avg": avg,
        "sum": total,
    }


def main():
    tests = [
        [1, 2, 3, 4],
        [-5, -1, -10],
        [10],
        [],
    ]

    for t in tests:
        print(f"in={t} -> out={stats(t)}")


if __name__ == "__main__":
    main()
