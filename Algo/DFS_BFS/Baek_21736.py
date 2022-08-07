import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

location = [0, 0]
campus = []

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for i in range(n):
    tmp = list(sys.stdin.readline().strip())

    for j in range(m):
        if tmp[j] == 'I':
            location[0] = j
            location[1] = i

    campus.append(tmp)

def bfs(x, y):
    que = deque()
    que.append((x, y))
    campus[y][x] = 'C'
    cnt = 0

    while que:
        now_x, now_y = que.popleft()

        for dir in range(4):
            nx = now_x + dx[dir]
            ny = now_y + dy[dir]

            if 0 <= nx < m and 0 <= ny < n:
                if campus[ny][nx] == 'O' or campus[ny][nx] == 'P':
                    if campus[ny][nx] == 'P':
                        cnt += 1
                    campus[ny][nx] = 'C'
                    que.append((nx, ny))

    return cnt

result = bfs(location[0], location[1])
if result > 0:
    print(result)
else:
    print("TT")