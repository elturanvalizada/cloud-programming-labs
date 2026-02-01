# S3_LAM_04 — Sum of squares of even numbers

from functools import reduce

def main():
    nums = [1, 2, 3, 4, 5, 6]

    evens = list(filter(lambda n: n % 2 == 0, nums))
    squares = list(map(lambda n: n * n, evens))
    total = reduce(lambda a, b: a + b, squares, 0)

    print("nums:", nums)
    print("evens:", evens)
    print("squares:", squares)
    print("sum of squares:", total)

    # Alternative (also acceptable):
    alt_total = sum(map(lambda n: n * n, filter(lambda n: n % 2 == 0, nums)))
    print("sum (using sum):", alt_total)


if __name__ == "__main__":
    main()
