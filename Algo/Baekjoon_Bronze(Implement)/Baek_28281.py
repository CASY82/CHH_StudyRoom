import sys

n, x = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))

res = sys.maxsize

for i in range(n - 1):
    res = min(res, x * cost[i] + x * cost[i + 1])

print(res)