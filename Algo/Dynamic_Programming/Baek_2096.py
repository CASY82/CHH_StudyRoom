# 메모리 초과
# n = int(sys.stdin.readline())
# board = []
# dp_max = [[0, 0, 0] for _ in range(n)]
# dp_min = [[0, 0, 0] for _ in range(n)]
#
# for _ in range(n):
#     board.append(list(map(int, sys.stdin.readline().split())))
#
# dp_max[0] = board[0]
# dp_min[0] = board[0]
#
# for i in range(1, n):
#     dp_max[i][0] = max(dp_max[i - 1][0], dp_max[i - 1][1]) + board[i][0]
#     dp_max[i][1] = max(dp_max[i - 1][0], dp_max[i - 1][1], dp_max[i - 1][2]) + board[i][1]
#     dp_max[i][2] = max(dp_max[i - 1][1], dp_max[i - 1][2]) + board[i][2]
#
#     dp_min[i][0] = min(dp_min[i - 1][0], dp_min[i - 1][1]) + board[i][0]
#     dp_min[i][1] = min(dp_min[i - 1][0], dp_min[i - 1][1], dp_min[i - 1][2]) + board[i][1]
#     dp_min[i][2] = min(dp_min[i - 1][1], dp_min[i - 1][2]) + board[i][2]
#
# print(max(dp_max[-1]), min(dp_min[-1]))

import sys

n = int(sys.stdin.readline())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
tmp = [0, 0, 0]

for i in range(n):
    board = list(map(int, sys.stdin.readline().split()))

    tmp[0] = max(dp_max[0], dp_max[1]) + board[0]
    tmp[1] = max(dp_max[0], dp_max[1], dp_max[2]) + board[1]
    tmp[2] = max(dp_max[1], dp_max[2]) + board[2]

    for j in range(3):
        dp_max[j] = tmp[j]

    tmp[0] = min(dp_min[0], dp_min[1]) + board[0]
    tmp[1] = min(dp_min[0], dp_min[1], dp_min[2]) + board[1]
    tmp[2] = min(dp_min[1], dp_min[2]) + board[2]

    for j in range(3):
        dp_min[j] = tmp[j]

print(max(dp_max), min(dp_min))

# 다른 사람 풀이(똑같네)
# import heapq
# import sys
#
#
# input = sys.stdin.readline
#
# n = int(input())
#
# first = list(map(int, input().split()))
#
# # max_arr = [first]
# # min_arr = [first]
#
# max_prev = first
# min_prev = first
#
# for idx in range(1, n):
#     t = list(map(int, input().split()))
#
#     max_1 = max(max_prev[0:2]) + t[0]
#     max_2 = max(max_prev) + t[1]
#     max_3 = max(max_prev[1:]) + t[2]
#
#     max_prev = [max_1, max_2, max_3]
#     # max_arr.append([max_1, max_2, max_3])
#
#     min_1 = min(min_prev[0:2]) + t[0]
#     min_2 = min(min_prev) + t[1]
#     min_3 = min(min_prev[1:]) + t[2]
#     min_prev = [min_1, min_2, min_3]
#     # min_arr.append([min_1, min_2, min_3])
#
# mmax = max(max_prev)
# mmin = min(min_prev)
#
# print(mmax, mmin)

#다른 사람 풀이2 : 똑같네... 한줄로 했을뿐, 배열 안쓰고

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# ma,mi = [0]*3,[0]*3
#
# for _ in range(N):
#     a,b,c = map(int, input().split())
#     ma[0],ma[1],ma[2] = max(ma[0],ma[1])+a,max(ma[0],ma[1],ma[2])+b,max(ma[1],ma[2])+c
#     mi[0],mi[1],mi[2] = min(mi[0],mi[1])+a,min(mi[0],mi[1],mi[2])+b,min(mi[1],mi[2])+c
#
# print(max(ma), min(mi))