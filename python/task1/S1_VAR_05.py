# S1_VAR_05 — Truthiness

def is_truthy(v):
    return bool(v)


def main():
    test_values = [
        0,
        1,
        "",
        "0",
        [],
        [0],
        {},
        None,
    ]

    for v in test_values:
        print(f"value={repr(v):<8} -> truthy={is_truthy(v)}")


if __name__ == "__main__":
    main()
