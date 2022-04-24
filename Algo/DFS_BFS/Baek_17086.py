import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
sea = []
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, 1, -1]
result = 0

for _ in range(n):
    sea.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y):
    que = deque()
    que.append((x, y, 1))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[y][x] = 1

    while que:
        tx, ty, cnt = que.popleft()

        for i in range(8):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0 and sea[ny][nx] != 1:
                    visited[ny][nx] = 1

                    if sea[ny][nx] > 0:
                        sea[ny][nx] = min(sea[ny][nx], cnt + 1)
                    else:
                        sea[ny][nx] = cnt + 1

                    que.append((nx, ny, cnt + 1))

for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            bfs(j, i)

for i in range(n):
    for j in range(m):
        if result < sea[i][j]:
            result = sea[i][j]

print(result-1)

# 아 뭐야 더 쉽게 하는 방법이 있다니;;;
# from collections import deque
# dx = [-1, -1, -1, 0, 1, 1, 1, 0]
# dy = [-1, 0, 1, 1, 1, 0, -1, -1]
#
# n, m = map(int, input().split())
# graph = list(list(map(int, input().split())) for _ in range(n))
#
# q = deque()
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             q.append((i,j))
#
# while q:
#     x, y = q.popleft()
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = graph[x][y] + 1
#                 q.append((nx, ny))
# answer = 0
# for i in range(n):
#     answer = max(answer, max(graph[i]))
# print(answer-1)

# 다른사람 풀이2
# from collections import deque
#
# def bfs():
#     maxv = 0
#     visited = [[0] * M for _ in range(N)]
#
#     while q:
#         ci, cj = q.popleft()
#
#         for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
#             ni, nj = ci+di, cj+dj
#             if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and not arr[ni][nj]:
#                 q.append([ni, nj])
#                 visited[ni][nj] = visited[ci][cj] + 1
#                 maxv = visited[ni][nj]
#     return maxv
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# q = deque()
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]:
#             q.append([i, j])
#
# print(bfs())