import sys

n = int(sys.stdin.readline())
res = 0

for _ in range(n):
    c, k = map(int, sys.stdin.readline().split())

    res += c * k

print(res)