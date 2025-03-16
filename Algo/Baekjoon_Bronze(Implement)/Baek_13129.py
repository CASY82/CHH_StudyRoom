import sys

a, b, n = map(int, sys.stdin.readline().split())
res = []

for i in range(1, n + 1):
    res.append((b * i) + (a * n))

print(*res)