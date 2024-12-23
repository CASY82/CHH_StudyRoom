# import sys
#
# n, m, k = map(int, sys.stdin.readline().split())
# seat = []
# res = 0
#
# for _ in range(n):
#     seat.append(list(sys.stdin.readline().strip()))
#
# for i in range(n):
#     j = 0
#     while j < (m - k + 1):
#         if seat[i][j] == "0":
#             check = True
#             for z in range(j, j + k):
#                 if seat[i][z] != "0":
#                     check = False
#                     j = z
#                     break
#             if check:
#                 res += 1
#         j += 1
#
# print(res)

import sys

n, m, k = map(int, sys.stdin.readline().split())
seat = []
res = 0

for _ in range(n):
    seat.append(list(sys.stdin.readline().strip()))

for i in range(n):
    j = 0
    count_zero = 0  # 현재 윈도우 내 '0'의 개수

    while j < m:
        # 윈도우에 '0'이 추가되는 경우
        if seat[i][j] == '0':
            count_zero += 1

        # 윈도우의 크기가 k를 초과하면 가장 왼쪽 요소를 제거
        if j >= k:
            if seat[i][j - k] == '0':
                count_zero -= 1

        # 현재 윈도우의 크기가 k일 때 '0'의 개수가 k와 같으면 결과 증가
        if j >= k - 1 and count_zero == k:
            res += 1

        j += 1

print(res)

# 다른 사람 풀이
# rows, columns, members = map(int, input().split())
#
# seats = []
# for x in range(rows):
#   y = input()
#   seats.append(y)
#
# ans = 0
# for x in seats:
#   counter = 0
#   for z in range(columns):
#     if x[z] == '1':
#       counter = 0
#     else:
#       counter += 1
#     if counter >= members:
#       ans += 1
#
# print(ans)