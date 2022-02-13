import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomato = deque()
box = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
result = 0

# tomato = [[list(sys.stdin.readline().split()) for _ in range(n)] for _ in range(h)]
for i in range(h):
    box.append([])
    for j in range(n):
        tmp_list = list(map(int, sys.stdin.readline().split()))
        box[i].append(tmp_list)

        #트메이러 좌표 입력
        for k in range(m):
            if tmp_list[k] == 1:
                tomato.append([k, j, i])

def bfs():
    while tomato:
        x, y, z = tomato.popleft()
        tmp = box[z][y][x]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = tmp + 1
                tomato.append([nx, ny, nz])

bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)

        result = max(max(box[i][j]), result)

print(result - 1)
