import sys

n, m, k = map(int, sys.stdin.readline().split())

remain_min = n - (m * k)
remain_max = remain_min + (m - 1)

if remain_max < 0:
    remain_max = 0

if remain_min < 0:
    remain_min = 0

print(remain_min, remain_max)