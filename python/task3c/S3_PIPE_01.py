# S3_PIPE_01 — Implement pipe(*fns)

def pipe(*fns):
    def runner(x):
        value = x
        for fn in fns:
            value = fn(value)
        return value
    return runner


def main():
    add2 = lambda n: n + 2
    times3 = lambda n: n * 3
    minus5 = lambda n: n - 5

    p = pipe(add2, times3, minus5)

    # ((10 + 2) * 3) - 5 = 31
    print("pipe result:", p(10))


if __name__ == "__main__":
    main()
