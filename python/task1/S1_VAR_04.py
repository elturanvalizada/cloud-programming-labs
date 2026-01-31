# S1_VAR_04 — Identity vs equality (is vs ==)

def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print("a == b:", a == b)   # True (same values)
    print("a is b:", a is b)   # False (different objects)
    print("a is c:", a is c)   # True (same object)

    x = None
    print("x is None:", x is None)   # Correct way to check None
    print("x == None:", x == None)   # Works but not recommended

    # Use is for identity, == for equality.


if __name__ == "__main__":
    main()
