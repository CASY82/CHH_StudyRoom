import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

banner = []
cnt = 0

for _ in range(m):
    banner.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def bfs(x, y):
    if banner[y][x] == 0 or banner[y][x] == 2:
        return False

    que = deque()
    que.append((x, y))

    while que:
        tx, ty = que.popleft()

        for i in range(8):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if banner[ny][nx] == 1:
                    banner[ny][nx] = 2
                    que.append((nx, ny))

    return True

for i in range(m):
    for j in range(n):
        if bfs(j, i):
            cnt += 1

print(cnt)