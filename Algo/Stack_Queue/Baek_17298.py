# 시간 초과
# import sys
#
# n = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
#
# stack = []
# result = [-1 for _ in range(n)]
# loc = 0
#
# for i in range(n):
#     for j in range(len(stack)-1, -1, -1):
#         if num_list[i] > stack[-1]:
#             result[num_list.index(stack[-1])] = num_list[i]
#             stack.pop()
#
#     stack.append(num_list[i])
#
# print(*result)

import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1 for _ in range(n)]

for i in range(n):
    while stack and num_list[i] > num_list[stack[-1]]:
        idx = stack.pop()
        result[idx] = num_list[i]

    stack.append(i)

print(*result)