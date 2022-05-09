import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
visited = [0 for i in range(n+1)]

for _ in range(m):
    start, dest = map(int, sys.stdin.readline().split())

    adj[start].append(dest)
    adj[dest].append(start)

for i in range(1, len(adj)):
    adj[i].sort()

#'정점 r에서 시작한다' 문구 안보고 했다가 틀림 이런!
def bfs(r):
    que = deque()
    que.append(r)
    visited[r] = 1
    cnt = 1

    while que:
        now = que.popleft()

        for i in adj[now]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                que.append(i)

bfs(r)
for i in range(1, len(visited)):
    print(visited[i])