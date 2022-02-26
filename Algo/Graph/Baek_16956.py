# import sys
#
# r, c = map(int, sys.stdin.readline().split())
# farm = []
#
# for _ in range(r):
#     farm.append(list(sys.stdin.readline().strip()))
#
# def dfs(x, y, check):
#     if x < 0 or y < 0 or x > r or y > c:
#         return False
#
#     if farm[y][x] == 'W':
#         dfs(x - 1, y, True)
#         dfs(x + 1, y, True)
#         dfs(x, y - 1, True)
#         dfs(x, y + 1, True)
#         return False
#
#     if check:
#         if farm[y][x] == '.':
#             farm[y][x] = 'D'
#             return False
#         else:
#             return True
#     return False
#
#
# result = 1
# for i in range(r):
#     for j in range(c):
#         if dfs(j, i, False):
#             result = 0
#             break
#
#     if result == 1:
#         break
#
# print(result)
# print(farm)

import sys

r, c = map(int, sys.stdin.readline().split())
farm = []

for _ in range(r):
    farm.append(list(sys.stdin.readline().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = True
for i in range(r):
    for j in range(c):
        if farm[i][j] == 'W':
            for k in range(4):
                mx = j+dx[k]
                my = i+dy[k]
                if 0 <= mx < c and 0 <= my < r:
                    if farm[my][mx] == ".":
                        farm[my][mx] = "D"
                    elif farm[my][mx] == "S":
                        flag = False
                        break
        if flag:
            continue

    if flag:
        continue

if flag:
    print(1)
    for i in range(r):
        for j in range(c):
            print(farm[i][j], end="")
        print()
else:
    print(0)