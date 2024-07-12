import sys

n = int(sys.stdin.readline())

tmp = [0, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1]

print(tmp[n])

# 다른 사람 풀이

# n = int(input())
#
# count = 0
# for i in range(6):
#     for j in range(i, 6):
#         if i + j == n:
#             count += 1
#
# print(count)