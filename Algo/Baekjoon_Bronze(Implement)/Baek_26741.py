import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

max_len = 1
now = 1

for i in range(1, n):
    if num_list[i] > num_list[i - 1]:
        now += 1
        max_len = max(max_len, now)
    else:
        max_len = max(max_len, now)
        now = 1

print(max_len)

# 다른 사람 풀이

# import math
# import random
# import sys
# import time
# from collections import defaultdict
#
# input = lambda: sys.stdin.readline().rstrip()
# ii = lambda: int(input())
# mii = lambda: map(int, input().split())
# mfi = lambda: map(float, input().split())
# lmii = lambda: list(map(int, input().split()))
# ni = lambda n: map(int, [ii() for _ in range(n)])
#
# n = ii()
# a = lmii()
# last = 0
# ans = 0
# for i in range(1, n):
#     if a[i] <= a[i - 1]:
#         ans = max(ans, i - last)
#         last = i
# ans = max(ans, n - last)
# print(ans)

# 다른 사람 풀이 2

# n = int(input())
# arr = list(map(int,input().split()))
#
# res,temp = 0,1
# for i in range(n-1):
#   if arr[i]<arr[i+1]:
#     temp+=1
#   else:
#     res = max(res,temp)
#     temp = 1
# res = max(res,temp)
# print(res)