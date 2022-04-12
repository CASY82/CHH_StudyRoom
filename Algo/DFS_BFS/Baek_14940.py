import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

land = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    land.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y):
    que = deque()
    que.append((x, y, 1))
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[y][x] = 0

    while que:
        tx, ty, dist = que.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == -1 and land[ny][nx] != 0:
                    visited[ny][nx] = dist
                    que.append((nx, ny, dist + 1))

    return visited

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            result = bfs(j, i)
            break

    if land[i][j] == 2:
        break

for i in range(n):
    for j in range(m):
        if land[i][j] == 0:
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()
