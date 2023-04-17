import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ladder = dict()
snake = dict()

visited = [True] * 101

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    ladder[x] = y

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    snake[u] = v

que = deque()
visited[1] = False
que.append((1, 0))

while que:
    now, cnt = que.popleft()

    if now == 100:
        print(cnt)
        break

    for dice in range(1, 7):
        moved = now + dice

        if moved <= 100 and visited[moved]:
            if moved in ladder:
                moved = ladder[moved]

            if moved in snake:
                moved = snake[moved]

            visited[moved] = False
            que.append((moved, cnt + 1))