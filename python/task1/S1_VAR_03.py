# S1_VAR_03 — Mutability: list vs tuple

def main():
    lst = [1, 2, 3]
    lst[0] = 99
    print("Modified list:", lst)

    tup = (1, 2, 3)
    try:
        tup[0] = 99
    except TypeError as e:
        print("Error modifying tuple:", e)

    # Lists are mutable (their contents can change),
    # tuples are immutable (their contents cannot be reassigned).


if __name__ == "__main__":
    main()
