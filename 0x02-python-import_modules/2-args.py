#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    else:
        print(f"{count} arguments.")
        for num in range(count):
            print(f"{num}: {sys.argv[num]}")
