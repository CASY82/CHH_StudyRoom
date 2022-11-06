import sys
import math

n = int(sys.stdin.readline())

print(int(math.sqrt(n)))
# 검증용 코드
#
# test = [0 for i in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j % i == 0:
#             if test[j] == 0:
#                 test[j] = 1
#             else:
#                 test[j] = 0
#
# print(test)
# print(sum(test))