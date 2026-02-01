# S2_LIST_06 — Transform records

def active_user_names(users):
    return sorted(
        [u["name"].upper() for u in users if u.get("active")]
    )


def main():
    users = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Charlie", "active": True},
        {"id": 4, "name": "dave", "active": True},
    ]

    print(active_user_names(users))


if __name__ == "__main__":
    main()
