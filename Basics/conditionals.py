def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    if x < y:
        print("x is less than y")
    elif x == y:
        print("x is eqaual to y")
    else:
        print("x is greater than y")

    # conditional statements let you use "a if C else b"
    print("x is less than y") if (x < y) else print("x is greater than or equal to y")


if __name__ == "__main__":
    main()
