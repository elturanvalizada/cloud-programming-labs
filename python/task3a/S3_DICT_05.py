# S3_DICT_05 — Invert dictionary with collisions

def invert(d):
    result = {}

    for key, value in d.items():
        if value in result:
            # value already exists → append key
            if isinstance(result[value], list):
                result[value].append(key)
            else:
                result[value] = [result[value], key]
        else:
            result[value] = key

    return result


def main():
    d1 = {"a": 1, "b": 1, "c": 2}
    d2 = {"x": "red", "y": "blue", "z": "red"}
    d3 = {}

    print(invert(d1))  # {1: ['a', 'b'], 2: 'c'}
    print(invert(d2))  # {'red': ['x', 'z'], 'blue': 'y'}
    print(invert(d3))  # {}


if __name__ == "__main__":
    main()
