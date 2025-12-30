import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
node = [[] for _ in range(n + 1)]
visited = [True for _ in range(n + 1)]
queue = deque()
res = 999999999999

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    node[x].append(y)
    node[y].append(x)

queue.append((1, 0))
visited[1] = False

while queue:
    now, cnt = queue.popleft()

    if now == n:
        res = min(cnt, res)
        break

    for i in node[now]:
        if visited[i]:
            visited[i] = False
            queue.append((i, cnt + 1))

if res == 999999999999:
    print(-1)
else:
    print(res)