# S1_VAR_01 — Catalog of values and type()

def sample_function():
    return "hello"


def main():
    values = [
        ("an_int", 42),
        ("a_float", 3.14),
        ("a_str", "python"),
        ("a_bool", True),
        ("a_none", None),
        ("a_list", [1, 2, 3]),
        ("a_tuple", (1, 2, 3)),
        ("a_dict", {"a": 1, "b": 2}),
        ("a_set", {1, 2, 3}),
        ("a_function", sample_function),
    ]

    print(f"{'name':<12} {'value':<25} {'type(x)':<25} {'type_name':<12}")
    print("-" * 80)

    for name, v in values:
        t = type(v)
        print(f"{name:<12} {repr(v):<25} {str(t):<25} {t.__name__:<12}")


if __name__ == "__main__":
    main()
