# S3_LAM_05 — Higher-order predicate

def at_least(min_value):
    return lambda x: x >= min_value


def main():
    nums = [1, 5, 8, 10, 3, 7]

    at_least_5 = at_least(5)
    at_least_8 = at_least(8)

    print("nums:", nums)
    print(">= 5:", list(filter(at_least_5, nums)))
    print(">= 8:", list(filter(at_least_8, nums)))


if __name__ == "__main__":
    main()
