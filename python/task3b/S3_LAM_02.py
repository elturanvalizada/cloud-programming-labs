# S3_LAM_02 — Sort by age using lambda

def main():
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 25},
        {"name": "Diana", "age": 28},
    ]

    print("Before sorting:")
    print(people)

    sorted_people = sorted(people, key=lambda p: p["age"])

    print("\nAfter sorting by age:")
    print(sorted_people)


if __name__ == "__main__":
    main()
