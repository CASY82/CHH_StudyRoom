import sys

x, l, r = map(int, sys.stdin.readline().strip().split())

min_diff = 99999999
res = 0

for num in range(l, r + 1):
    if min_diff > abs(x - num):
        res = num
        min_diff = abs(x - num)

print(res)