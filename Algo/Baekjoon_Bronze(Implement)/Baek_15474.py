import sys

n, a, b, c, d = map(int, sys.stdin.readline().split())

a_tmp = 0
c_tmp = 0

a_cost = 0
c_cost = 0

while True:
    if a_tmp < n:
        a_cost += b
        a_tmp += a

    if c_tmp < n:
        c_cost += d
        c_tmp += c

    if a_tmp >= n and c_tmp >= n:
        break

print(min(c_cost, a_cost))

# 다른 사람 풀이
# import math
#
# N, A, B, C, D=map(int, input().split())
#
# pay=min(math.ceil(N/A)*B, math.ceil(N/C)*D)
# print(pay)