# S3_DICT_01 — Safe get by dotted path

def get_path(obj, path, fallback=None):
    if not isinstance(obj, dict):
        return fallback

    current = obj
    for part in path.split("."):
        if not isinstance(current, dict):
            return fallback
        if part not in current:
            return fallback
        current = current[part]

    return current


def main():
    data = {
        "a": {
            "b": {
                "c": 123
            }
        },
        "x": 5
    }

    print(get_path(data, "a.b.c", "N/A"))   # 123
    print(get_path(data, "a.b.z", "N/A"))   # N/A (missing key)
    print(get_path(data, "x.y", "N/A"))     # N/A (x is not dict)
    print(get_path("not dict", "a.b", "N/A"))  # N/A


if __name__ == "__main__":
    main()
