# S3_PIPE_06 — Safe pipeline (pipe_safe)

def pipe_safe(*fns):
    def runner(x):
        value = x
        try:
            for fn in fns:
                value = fn(value)
            return {"ok": True, "value": value}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return runner


def main():
    def to_int(s):
        return int(s)  # raises ValueError on bad input

    def double(n):
        return n * 2

    safe = pipe_safe(to_int, double)

    print("good:", safe("21"))   # ok True, value 42
    print("bad:", safe("xx"))    # ok False, error message


if __name__ == "__main__":
    main()
