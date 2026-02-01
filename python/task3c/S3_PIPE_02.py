# S3_PIPE_02 — Implement compose(*fns)

def compose(*fns):
    def runner(x):
        value = x
        for fn in reversed(fns):
            value = fn(value)
        return value
    return runner


def main():
    add2 = lambda n: n + 2
    times3 = lambda n: n * 3
    minus5 = lambda n: n - 5

    # pipe: left → right
    def pipe(*fns):
        def r(x):
            for fn in fns:
                x = fn(x)
            return x
        return r

    p = pipe(add2, times3, minus5)
    c = compose(add2, times3, minus5)

    print("pipe result:", p(10))      # ((10+2)*3)-5 = 31
    print("compose result:", c(10))   # add2(times3(minus5(10))) = 17


if __name__ == "__main__":
    main()
