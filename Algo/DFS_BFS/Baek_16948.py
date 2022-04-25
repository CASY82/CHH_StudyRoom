import sys
from collections import deque

n = int(sys.stdin.readline())

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

chess = [[0 for _ in range(n)] for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y, 0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[y][x] = 1

    while que:
        tx, ty, cnt = que.popleft()

        if tx == r2 and ty == c2:
            return cnt

        for i in range(6):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    que.append((nx, ny, cnt + 1))

    return -1

print(bfs(r1, c1))