# 교환 분배법칙
# import sys
#
# n = int(sys.stdin.readline())
# cnt = 0
#
# for a in range(-n, n + 1):
#     for b in range(-n, n + 1):
#         for c in range(-n, n + 1):
#             if (a + b) * (a + c) == a + (b * c):
#                 cnt += 1
#
# print(cnt)

import sys

n = int(sys.stdin.readline())

# a = 0일 때 : b, c의 모든 조합
# a + b + c - 1 = 0일 때 : 음수를 포함해서 a + b + c = 1인 조합합
print(7 * n * n + 5 * n + 1)