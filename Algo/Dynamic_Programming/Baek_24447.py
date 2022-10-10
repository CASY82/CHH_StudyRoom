# 순서를 구해야하는 부분을 잘못이해해서 한번 틀렸음;;
import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(n+1)]
visited = [True for _ in range(n+1)]
depth = [-1 for _ in range(n+1)]
seq = [0 for _ in range(n+1)]
result = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    nodes[u].append(v)
    nodes[v].append(u)

def bfs(start):
    que = deque()
    que.append((start, 0))
    visited[start] = False
    depth[start] = 0
    order = 1
    seq[start] = order


    while que:
        now, dept = que.popleft()

        nodes[now].sort()

        for nxt in nodes[now]:
            if visited[nxt]:
                order += 1
                visited[nxt] = False
                seq[nxt] = order
                depth[nxt] = dept + 1
                que.append((nxt, dept + 1))

bfs(r)

for i in range(1, n+1):
    result += depth[i] * seq[i]

print(result)