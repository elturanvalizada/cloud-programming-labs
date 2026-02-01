# S3_DICT_03 — Pick keys

def pick(d, keys):
    result = {}
    for k in keys:
        if k in d:
            result[k] = d[k]
    return result


def main():
    d = {"a": 1, "b": 2, "c": 3}
    print(pick(d, ["a", "c"]))          # {'a': 1, 'c': 3}
    print(pick(d, ["a", "x", "b"]))     # {'a': 1, 'b': 2}
    print(pick(d, []))                  # {}


if __name__ == "__main__":
    main()
