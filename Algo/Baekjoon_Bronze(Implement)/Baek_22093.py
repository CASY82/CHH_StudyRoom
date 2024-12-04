import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, a, b = map(int, sys.stdin.readline().split())

    low = max(a - b, 0)
    high = min(n - b, a)

    print(low, high)