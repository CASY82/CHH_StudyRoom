# dfs로 접근해야함

# import sys
# from collections import deque
#
# r, c = map(int, sys.stdin.readline().split())
# line_map = []
# cnt = [0]
#
# for _ in range(r):
#     line_map.append(list(sys.stdin.readline().strip()))
#
# def bfs(row):
#     que = deque()
#     que.append((0, row))
#
#     while que:
#         print(line_map)
#         x, y = que.popleft()
#
#         if x == c - 1:
#             cnt[0] += 1
#             break
#
#         for i in (1, 0, -1):
#             if x + 1 < c and 0 <= y + i < r:
#                 if line_map[y + i][x + 1] == 'x':
#                     continue
#                 elif line_map[y + i][x + 1] == '.':
#                     line_map[y + i][x + 1] = '0'
#                     que.append((x+1, y+i))
#                     break
#
#
# for i in range(r):
#     bfs(i)
#
# print(cnt)

import sys

r, c = map(int, sys.stdin.readline().split())
line_map = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
cnt = 0

def dfs(x, y):
    if x == c - 1:
        return True
    for j in (-1, 0, 1):
        nx = x + 1
        ny = y + j
        if (0 <= nx < c) and (0 <= ny < r) and not visit[ny][nx] and line_map[ny][nx] == '.':
            visit[ny][nx] = True
            if dfs(nx, ny):
                return True

    return False

for i in range(r):
    if line_map[i][0] == '.':
        if dfs(0, i):
            cnt += 1

print(cnt)
