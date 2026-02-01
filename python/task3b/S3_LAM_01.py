# S3_LAM_01 — Convert to lambdas

square = lambda n: n * n
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"


def main():
    # square tests
    print("square tests:")
    print(square(2))   # 4
    print(square(5))   # 25
    print(square(-3))  # 9

    # is_odd tests
    print("\nis_odd tests:")
    print(is_odd(1))   # True
    print(is_odd(2))   # False
    print(is_odd(11))  # True

    # greet tests
    print("\ngreet tests:")
    print(greet("Ala"))
    print(greet("Ola"))
    print(greet("Elturan"))


if __name__ == "__main__":
    main()
