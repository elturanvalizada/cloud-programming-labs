# S1_VAR_08 — Big integers in Python

def main():
    big_int = 10 ** 100
    big_float = float(big_int)

    print("Big integer:", big_int)
    print("Type:", type(big_int).__name__)
    print("Number of digits:", len(str(big_int)))

    print("\nBig float:", big_float)
    print("Type:", type(big_float).__name__)

    # Python integers have arbitrary precision,
    # while floats lose precision for very large numbers.


if __name__ == "__main__":
    main()
