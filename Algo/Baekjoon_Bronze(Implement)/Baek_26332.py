import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c, p = map(int, sys.stdin.readline().split())

    total = (p * c) - ((c - 1) * 2)

    print(c, p)
    print(total)