import sys
sys.setrecursionlimit(10 ** 5)

node, edge = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(node)]
cnt = 0

for i in range(edge):
    src, dest = map(int, sys.stdin.readline().split())

    adj[src-1].append(dest)
    adj[dest-1].append(src)

visited = [False for _ in range(node+1)]

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v-1]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

for i in range(node):
    if not visited[i]:
        dfs(adj, i, visited)
        cnt += 1

print(cnt)