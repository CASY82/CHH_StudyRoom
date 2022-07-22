import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    nodes[u].append(v)
    nodes[v].append(u)

def bfs(start):
    que = deque()
    que.append(start)
    visited = [True for _ in range(n)]
    visited[start-1] = False
    cnt = 1
    result[start] = cnt

    while que:
        now = que.popleft()

        tmp = sorted(nodes[now], reverse=True)

        for i in tmp:
            if visited[i-1]:
                visited[i-1] = False
                cnt += 1
                result[i] = cnt
                que.append(i)

bfs(r)

for i in range(1, n+1):
    print(result[i])