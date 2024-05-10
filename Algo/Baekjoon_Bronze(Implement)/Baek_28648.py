import sys

n = int(sys.stdin.readline())
min_res = 999999

for _ in range(n):
    ti, li = map(int, sys.stdin.readline().split())

    min_res = min(min_res, ti + li)

print(min_res)