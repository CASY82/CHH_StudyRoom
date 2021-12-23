import sys

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
adj = [[] for i in range(node)]

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().split())

    adj[src-1].append(dest)
    adj[dest-1].append(src)

visited = [False for _ in range(node+1)]

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v-1]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(adj, 1, visited)
print(visited.count(True)-1)