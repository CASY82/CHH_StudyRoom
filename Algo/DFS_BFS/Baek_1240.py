## 문제를 풀기만 하면되나 시간이 없어
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
#
# nodes = [[] for _ in range(n + 1)]
#
# for _ in range(n):
#     u, v, weight = map(int, sys.stdin.readline().split())
#     nodes[u].append([v, weight])
#     nodes[v].append([u, weight])


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

def dist(u, v):
    # BFS (DFS로 바꿔도 동일)
    q = deque([(u, 0)])
    visited = [False]*(N+1)
    visited[u] = True
    while q:
        x, d = q.popleft()
        if x == v:
            return d
        for nx, w in g[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, d+w))
    return -1  # 이론상 트리라 도달 불가 없음

out = []
for _ in range(M):
    u, v = map(int, input().split())
    out.append(str(dist(u, v)))
print("\n".join(out))