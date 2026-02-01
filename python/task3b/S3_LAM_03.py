# S3_LAM_03 — Closure factory

def make_adder(x):
    return lambda n: n + x


def main():
    add10 = make_adder(10)
    add3 = make_adder(3)

    print("add10 tests:")
    print(add10(5))    # 15
    print(add10(0))    # 10
    print(add10(-2))   # 8

    print("\nadd3 tests:")
    print(add3(7))     # 10
    print(add3(0))     # 3
    print(add3(-3))    # 0


if __name__ == "__main__":
    main()
