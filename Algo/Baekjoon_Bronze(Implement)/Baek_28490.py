import sys

t = int(sys.stdin.readline())
res = 0

for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())

    res = max(res, h * w)

print(res)