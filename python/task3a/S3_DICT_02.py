# S3_DICT_02 — Merge defaults (shallow)

def merge_defaults(defaults, overrides):
    # Shallow merge: top-level keys merged, nested dicts are not deep-merged
    return defaults | overrides


def main():
    defaults = {
        "timeout": 30,
        "retries": 3,
        "db": {"host": "localhost", "port": 5432},
    }
    overrides = {
        "timeout": 10,
        "db": {"host": "prod-db"},  # replaces whole nested dict (shallow)
    }

    merged = merge_defaults(defaults, overrides)

    print("defaults:", defaults)
    print("overrides:", overrides)
    print("merged:", merged)

    # Shallow merge example:
    # merged["db"] is exactly overrides["db"], so "port" is lost (not deep-merged)
    print("merged db port:", merged["db"].get("port"))  # None


if __name__ == "__main__":
    main()
