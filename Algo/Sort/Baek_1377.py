# import sys
# input = sys.stdin.readline
#
# N = int(input())
# A = [0]
# for _ in range(N):
#     A.append(int(input()))
#
# print(A)
#
# for i in range(1, N + 1):
#     changed = False
#     for j in range(1, N - i + 1):
#         if A[j] > A[j + 1]:
#             A[j], A[j + 1] = A[j + 1], A[j]
#             changed = True
#     if not changed:
#         print(i)
#         break

import sys

n = int(sys.stdin.readline())
a = []
res = 0

for index in range(n):
    num = int(sys.stdin.readline())
    a.append((num, index))

a.sort(key=lambda x:x[0])

for i in range(n):
    res = max(res, a[i][1] - i)

print(res + 1)