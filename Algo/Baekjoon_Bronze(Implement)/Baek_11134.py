import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    if a % b == 0:
        print(a // b)
    else:
        print(a // b + 1)