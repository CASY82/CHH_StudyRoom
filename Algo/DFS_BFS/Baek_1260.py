import sys
from collections import deque

node, edge, start = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(node)]

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().split())

    adj[src-1].append(dest)
    adj[dest-1].append(src)

for i in range(len(adj)):
    adj[i].sort()

visited_dfs = [False] * (len(adj)+1)
visited_bfs = [False] * (len(adj)+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v-1]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n-1]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

dfs(adj, start, visited_dfs)
print()
bfs(adj, start, visited_bfs)
