import sys

n, x, y = map(int, sys.stdin.readline().split())

for _ in range(n):
    a = int(sys.stdin.readline())

    print(a * y // x)