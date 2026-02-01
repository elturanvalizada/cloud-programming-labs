# S3_DICT_04 — Omit keys

def omit(d, keys):
    result = {}
    for k, v in d.items():
        if k not in keys:
            result[k] = v
    return result


def main():
    d = {"a": 1, "b": 2, "c": 3}
    print(omit(d, ["b"]))          # {'a': 1, 'c': 3}
    print(omit(d, ["a", "c"]))     # {'b': 2}
    print(omit(d, []))             # {'a': 1, 'b': 2, 'c': 3}


if __name__ == "__main__":
    main()
