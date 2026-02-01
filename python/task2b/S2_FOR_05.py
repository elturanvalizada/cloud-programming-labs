# S2_FOR_05 — Multiplication table 10×10

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()  # new line after each row


if __name__ == "__main__":
    main()
