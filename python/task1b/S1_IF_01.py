# S1_IF_01 — Shipping cost

def shipping_cost(weight_kg, is_member):
    # Validate weight
    try:
        w = float(weight_kg)
    except (TypeError, ValueError):
        return None

    if w <= 0:
        return None

    if w <= 1:
        cost = 10
    elif w <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8  # 20% discount

    return cost


def main():
    tests = [
        (0, False),       # invalid
        (-1, True),       # invalid
        ("x", False),     # invalid
        (1, False),       # boundary -> 10
        (1, True),        # boundary + member -> 8
        (5, False),       # boundary -> 20
        (5, True),        # boundary + member -> 16
        (5.1, False),     # -> 30
    ]

    for w, m in tests:
        print(f"weight={w!r:>5}, member={m} -> {shipping_cost(w, m)}")


if __name__ == "__main__":
    main()
