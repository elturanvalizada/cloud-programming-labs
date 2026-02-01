# S1_VAR_10 — Mini inspector

from pprint import pprint

def inspect(v):
    # is_iterable: try iter(v) safely
    try:
        iter(v)
        is_iter = True
    except TypeError:
        is_iter = False

    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": is_iter,
        "truthy": bool(v),
    }


def main():
    values = [
        0,
        1,
        "",
        "hi",
        [],
        [0],
        {},
        {"a": 1},
        None,
        lambda x: x,
        (1, 2),
    ]

    for v in values:
        print(f"\nvalue = {repr(v)}")
        pprint(inspect(v))


if __name__ == "__main__":
    main()
