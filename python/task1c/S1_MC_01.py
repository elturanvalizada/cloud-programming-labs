# S1_MC_01 — Day name using match/case (Python 3.10+)

def day_name(n: int):
    match n:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _: return None


def main():
    tests = [0, 1, 2, 5, 7, 8, None]
    for t in tests:
        print(f"day_name({t!r}) -> {day_name(t)}")


if __name__ == "__main__":
    main()
# S1_MC_01 — Day name using match/case (Python 3.10+)

def day_name(n: int):
    match n:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _: return None


def main():
    tests = [0, 1, 2, 5, 7, 8, None]
    for t in tests:
        print(f"day_name({t!r}) -> {day_name(t)}")


if __name__ == "__main__":
    main()
