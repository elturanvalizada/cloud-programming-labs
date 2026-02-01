# S1_MC_03 — Simple calculator using match/case

def calc(a, op, b):
    # validate numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


def main():
    tests = [
        (10, "+", 5),
        (10, "-", 5),
        (10, "*", 5),
        (10, "/", 5),
        (10, "/", 0),
        ("10", "+", 5),
        (10, "?", 5),
    ]

    for a, op, b in tests:
        print(f"{a} {op} {b} -> {calc(a, op, b)}")


if __name__ == "__main__":
    main()
