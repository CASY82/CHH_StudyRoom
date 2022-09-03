import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
visited = [True for _ in range(n+1)]
result = [-1 for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    que = deque()
    visited[start] = False
    cnt = 0
    result[start] = cnt
    que.append((start, cnt))

    while que:
        now, cnt = que.popleft()
        cnt += 1

        for i in adj[now]:
            if visited[i]:
                visited[i] = False
                que.append((i, cnt))
                result[i] = cnt

bfs(r)
for i in range(1, len(result)):
    print(result[i])