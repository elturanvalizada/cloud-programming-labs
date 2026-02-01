# S2_FOR_01 — FizzBuzz+ (N=30)

def main():
    N = 30
    for i in range(1, N + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    main()
