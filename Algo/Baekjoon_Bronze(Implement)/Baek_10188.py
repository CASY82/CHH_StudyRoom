import sys

t = int(sys.stdin.readline())

for _ in range(t):
    col, row = map(int, sys.stdin.readline().split())

    for i in range(row):
        for j in range(col):
            print("X", end="")
        print()

    print()