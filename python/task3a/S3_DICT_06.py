# S3_DICT_06 — Group by property

def group_by(items, key):
    groups = {}
    for item in items:
        value = item.get(key)
        if value in groups:
            groups[value].append(item)
        else:
            groups[value] = [item]
    return groups


def main():
    people = [
        {"name": "Ala", "role": "dev"},
        {"name": "Ola", "role": "dev"},
        {"name": "Mika", "role": "qa"},
        {"name": "Sara", "role": "pm"},
        {"name": "John", "role": "qa"},
    ]

    grouped = group_by(people, "role")
    print(grouped)


if __name__ == "__main__":
    main()
