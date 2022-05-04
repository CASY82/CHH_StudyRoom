# 투 포인터 왜 틀리지?
# import sys
#
# n, k = map(int, sys.stdin.readline().split())
#
# temperature = list(map(int, sys.stdin.readline().split()))
#
# max_temp = -1000
# interval_sum = 0
# count = 0
# end = 0
#
# for start in range(n):
#     while count < k and end < n:
#         interval_sum += temperature[end]
#         count += 1
#         end += 1
#
#     if interval_sum > max_temp:
#         if count == k:
#             max_temp = interval_sum
#
#     interval_sum -= temperature[start]
#     count -= 1
#
#     print(max_temp)

import sys

n, k = map(int, sys.stdin.readline().split())

temperature = list(map(int, sys.stdin.readline().split()))

max_temp = -1000


for i in range(n-k+1):
    interval_sum = 0
    for j in range(i, i+k):
        interval_sum += temperature[j]

    if max_temp < interval_sum:
        max_temp = interval_sum

print(max_temp)