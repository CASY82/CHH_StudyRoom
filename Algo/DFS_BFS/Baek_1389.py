import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]
result = [0 for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    adj[a].append(b)
    adj[b].append(a)

def bfs(start, end):
    que = deque()
    que.append((start, 0))
    visited = [True for _ in range(n+1)]

    while que:
        now, cnt = que.popleft()

        if now == end:
            return cnt

        for i in adj[now]:
            if visited[i]:
                visited[i] = False
                que.append((i, cnt + 1))

    return 0

for i in range(1, n+1):
    for j in range(1, n+1):
        result[i-1] += bfs(i, j)

print(result.index(min(result))+1)