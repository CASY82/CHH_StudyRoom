import sys

r = int(sys.stdin.readline())
c = int(sys.stdin.readline())

for _ in range(r):
    for _ in range(c):
        print("*", end="")
    print()