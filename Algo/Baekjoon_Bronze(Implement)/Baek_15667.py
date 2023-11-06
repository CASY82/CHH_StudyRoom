import sys
import math

n = int(sys.stdin.readline())

tmp = 1 - (4 * (1 - n))
result_plus = ((-1) + math.sqrt(tmp)) // 2
result_minus = ((-1) - math.sqrt(tmp)) // 2

print(max(int(result_plus), int(result_minus)))

# 다른 사람 풀이
# n = int(input())
#
# for i in range(1, n + 1):
#     if i**2 + i + 1 - n == 0:
#         break
# print(i)