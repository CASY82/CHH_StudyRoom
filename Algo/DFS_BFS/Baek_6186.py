import sys
sys.setrecursionlimit(3000000)

def dfs(x, y, r, c):
    if 0 <= x < c and 0 <= y < r:
        if visit[y][x] == 0 and grass[y][x] == "#":
            visit[y][x] = 1
            dfs(x + 1, y, r, c)
            dfs(x, y + 1, r, c)
            dfs(x - 1, y, r, c)
            dfs(x, y - 1, r, c)

        return

r, c = map(int, sys.stdin.readline().split())
grass = []
visit = [[0 for _ in range(c)] for _ in range(r)]
res = 0

for _ in range(r):
    grass.append(list(sys.stdin.readline().strip()))

for i in range(r):
    for j in range(c):
        if grass[i][j] == "#" and visit[i][j] == 0: # 여기 불필요해보인다..?
            dfs(j, i, r, c)
            res += 1

print(res)

# 다른 사람 풀이
# from collections import deque
# MOVE = [[0,1],[-1,0],[0,-1],[1,0]]
#
#
# def bfs(i,j):
#     queue = deque()
#     queue.append((i,j))
#
#     while queue:
#         x, y = queue.popleft()
#         visited[x][y] = True
#
#         for move in MOVE:
#             nx, ny = x + move[0], y + move[1]
#             if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]=="#" and not visited[nx][ny]:
#                 queue.append((nx,ny))
#
#
#
# N, M = map(int, input().split())
# arr  = [input() for _ in range(N)]
# visited = [[False]*M for _ in range(N)]
#
# count = 0
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == "#" and not visited[i][j]:
#             bfs(i,j)
#             count += 1
#
# print(count)