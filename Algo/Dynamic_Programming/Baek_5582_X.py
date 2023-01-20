import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

# 메모리 초과
# c = [[0] * (len(second)+1) for _ in range(len(first)+1)]
#
# def lcs(m, n):
#     result = 0
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if first[i-1] == second[j-1]:
#                 c[i][j] = c[i-1][j-1] + 1
#                 result = max(c[i][j], result)
#
#     return result
#
# print(lcs(len(first), len(second)))

pre = [0] * (len(second) + 1)
result = 0

for i in range(len(first)):
    tmp = [0] * (len(second)+1)
    for j in range(len(second)):
        if first[i] == second[j]:
            tmp[j+1] = pre[j] + 1

    result = max(result, max(tmp))
    pre = tmp[:]

print(result)