# S1_IF_02 — Score to grade

def grade(score):
    try:
        s = float(score)
    except (TypeError, ValueError):
        return None

    if s < 0 or s > 100:
        return None

    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 60:
        return "D"
    else:
        return "F"


def main():
    tests = [59, 60, 69, 70, 89, 90, 100, 101]

    for t in tests:
        print(f"score={t:>3} -> grade={grade(t)}")


if __name__ == "__main__":
    main()
