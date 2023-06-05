import sys
from collections import deque

map_of_cow = []
visited = [[True for _ in range(10)] for _ in range(10)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    que = deque()
    visited[y][x] = False
    que.append((x, y, 0))

    while que:
        lx, ly, cnt = que.popleft()

        if map_of_cow[ly][lx] == 'B':
            return cnt

        if map_of_cow[ly][lx] == 'R':
            continue

        for next in range(4):
            nx = dx[next] + lx
            ny = dy[next] + ly

            if 0 <= nx < 10 and 0 <= ny < 10:
                if visited[ny][nx]:
                    que.append((nx, ny, cnt + 1))
                    visited[ny][nx] = False

for _ in range(10):
    map_of_cow.append(list(sys.stdin.readline().strip()))

for i in range(10):
    for j in range(10):
        if map_of_cow[i][j] == 'L':
            print(bfs(j, i) - 1)