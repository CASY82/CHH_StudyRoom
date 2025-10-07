import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

s, t = map(int, sys.stdin.readline().split())

INF = 10 ** 18
dist = [INF] * (n + 1)
dist[s] = 0

pq = [(0, s)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    if u == t:
        break

    for v, w in nodes[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[t])