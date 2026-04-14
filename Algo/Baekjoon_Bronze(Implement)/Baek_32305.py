# Farmers' market
import sys

a, b = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())

tmp = a * b
if tmp % 12 == 0:
    res = (tmp // 12) * d
else:
    res = (tmp // 12 + 1) * d

print(res)