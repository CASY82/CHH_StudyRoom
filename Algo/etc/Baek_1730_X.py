# 3%에서 자꾸 틀림(반례가 있나봄)
# import sys
#
# n = int(sys.stdin.readline())
# moving = sys.stdin.readline().strip()
#
# board = [[chr(46) for _ in range(n)] for _ in range(n)]
#
# # . | - +
# # chr(46), chr(124), chr(45), chr(43)
# direct = ["U", "D", "L", "R"]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# nx, ny = 0, 0
#
# for i in range(len(moving)):
#     tx = dx[direct.index(moving[i])] + nx
#     ty = dy[direct.index(moving[i])] + ny
#
#     if tx < 0 or tx >= n or ty < 0 or ty >= n:
#         continue
#
#     if board[ny][nx] == chr(46) and board[ty][tx] == chr(46):
#         if moving[i] in ["U", "D"]:
#             board[ny][nx] = chr(124)
#             board[ty][tx] = chr(124)
#         elif moving[i] in ["L", "R"]:
#             board[ny][nx] = chr(45)
#             board[ty][tx] = chr(45)
#     else:
#         if moving[i] in ["U", "D"]:
#             if board[ny][nx] == chr(45):
#                 board[ny][nx] = chr(43)
#
#             if board[ty][tx] == chr(45):
#                 board[ty][tx] = chr(43)
#             else:
#                 board[ty][tx] = chr(124)
#
#         elif moving[i] in ["L", "R"]:
#             if board[ny][nx] == chr(124):
#                 board[ny][nx] = chr(43)
#
#             if board[ty][tx] == chr(124):
#                 board[ty][tx] = chr(43)
#             else:
#                 board[ty][tx] = chr(45)
#
#     nx = tx
#     ny = ty
#
#     # print("i", i, "nx", nx, "ny", ny, "tx", tx, "ty", ty)
#     # for i in range(n):
#     #     for j in range(n):
#     #         print(board[i][j], end="")
#     #     print("")
#     # print("-----------------------")
#
#
# for i in range(n):
#     for j in range(n):
#         print(board[i][j], end="")
#     print()

n = int(input())
move = input()
draw = [['.' for _ in range(n)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
pos = [0, 0]

for i in range(len(move)):
    if move[i] == 'R':
        if pos[0] == n - 1:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[2]
        pos[1] += dy[2]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'

    elif move[i] == 'L':
        if pos[0] == 0:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[0]
        pos[1] += dy[0]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'

    elif move[i] == 'U':
        if pos[1] == 0:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[3]
        pos[1] += dy[3]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
    else:
        if pos[1] == n - 1:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[1]
        pos[1] += dy[1]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'

for i in range(n):
    print(''.join(draw[i]))