# S1_VAR_09 — Type hints are not runtime enforcement

def add(a: int, b: int) -> int:
    return a + b


def main():
    print(add(2, 3))          # correct usage
    print(add("2", "3"))      # incorrect types, but still works at runtime

    # Type hints are for readability and static analysis tools,
    # not automatic runtime type enforcement.


if __name__ == "__main__":
    main()
