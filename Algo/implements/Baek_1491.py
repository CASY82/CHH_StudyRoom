import sys

x, y = map(int, sys.stdin.readline().split())

board = [[0 for _ in range(x)] for _ in range(y)]

direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
direction_index = 0

start_x, start_y = 0, y-1
num = 1

for lastcheck in range(x*y):
    board[start_y][start_x] = num
    num += 1

    next_x = start_x + direction[direction_index][1]
    next_y = start_y + direction[direction_index][0]

    if(next_y < 0 or next_x < 0 or next_x >= x or next_y >= y or board[next_y][next_x] != 0):
        direction_index = (direction_index + 1) % 4

    if lastcheck == x*y-1:
        print(start_x, y-1-start_y)

    start_x += direction[direction_index][1]
    start_y += direction[direction_index][0]

#다른 사람 풀이
# import sys
#
# c, r = map(int, sys.stdin.readline().split())
# r -= 1
# c -= 1
# nx, ny = 0, 0
# ny += c
# flag = 1
# dx = 0
# dy = 0
# while True:
#     if flag == 1:
#         if r == 0:
#             break
#         if dx == 0:
#             nx += r
#             dx = 1
#         else:
#             nx -= r
#             dx = 0
#         r -= 1
#         flag = 0
#     else:
#         if c == 0:
#             break
#         if dy == 0:
#             ny -= c
#             dy = 1
#         else:
#             ny += c
#             dy = 0
#         c -= 1
#         flag = 1
# print(ny, nx)

# def snail(W,H):
#     top = 0
#     bottom = H-1
#     left = 0
#     right = W-1
#
#     dir = 0
#
#     while True:
#         if (dir == 0):
#             if (top == bottom):
#                 return right, top
#             top += 1
#         elif (dir == 1):
#             if (left == right):
#                 return right, bottom
#             right -= 1
#         elif (dir == 2):
#             if (top == bottom):
#                 return left, bottom
#             bottom -= 1
#         elif (dir == 3):
#             if (left == right):
#                 return left, top
#             left += 1
#         dir = (dir+1) % 4
#
#
# W, H = map(int, input().split())
# x,y=snail(W,H)
# print(x,y)