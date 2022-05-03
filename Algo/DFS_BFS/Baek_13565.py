# import sys
# sys.setrecursionlimit(300000)
#
# m, n = map(int, sys.stdin.readline().split())
#
# figure = []
#
# for _ in range(m):
#     figure.append(list(sys.stdin.readline().strip()))
#
# def dfs(x, y):
#     if x >= n or y >= m or x < 0 or y < 0:
#         return False
#
#     if figure[y][x] == '0':
#         figure[y][x] = '2'
#         dfs(x + 1, y)
#         dfs(x - 1, y)
#         dfs(x, y + 1)
#         dfs(x, y - 1)
#         return True
#
#     return False
#
# for i in range(n):
#     dfs(i, 0)
#
# if '2' in figure[-1]:
#     print("YES")
# else:
#     print("NO")

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

result = True
figure = []

for _ in range(m):
    figure.append(list(sys.stdin.readline().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x):
    que = deque()
    que.append((x, 0))

    while que:
        tx, ty = que.popleft()

        if ty == m-1:
            return True

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if figure[ny][nx] == '0':
                    figure[ny][nx] = '2'
                    que.append((nx, ny))

    return False

for i in range(n):
    if figure[0][i] == '0':
        if bfs(i):
            result = False

if result:
    print("NO")
else:
    print("YES")