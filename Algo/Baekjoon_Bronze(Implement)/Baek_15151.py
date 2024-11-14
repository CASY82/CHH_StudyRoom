import sys

k, d = map(int, sys.stdin.readline().split())

total = 0
res = 0

while True:
    total += k
    if total <= d:
        res += 1
    else:
        break
    k *= 2

print(res)

# 다른 사람 풀이
# import math
# k,d=map(int,open(0).read().split())
# print(math.floor(math.log2(d/k + 1)))