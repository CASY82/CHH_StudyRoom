import sys

n = int(sys.stdin.readline())

for _ in range(n):
    for _ in range(n * 5):
        print("@", end="")
    print()

for _ in range(n):
    for _ in range(n):
        print("@", end="")
    print()

for _ in range(n):
    for _ in range(n * 5):
        print("@", end="")
    print()

for _ in range(n * 2):
    for _ in range(n):
        print("@", end="")
    print()