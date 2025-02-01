import sys

n, m = map(int, sys.stdin.readline().split())
people = list(map(int, sys.stdin.readline().split()))
friend = set(map(int, sys.stdin.readline().split()))
res = 0

people = people[:m]

for i in range(m):
    if people[i] not in friend:
        res += 1

print(res)

# 다른 사람 풀이
# import sys
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# friend = list(map(int, input().split()))
# arr = list(map(lambda x: int(x in friend), arr))
# cnt = 0
# for i in range(n):
#     if arr[i] == 0:
#         for j in range(n - 1, i, -1):
#             if arr[j] == 1:
#                 cnt += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#                 break
# print(cnt)