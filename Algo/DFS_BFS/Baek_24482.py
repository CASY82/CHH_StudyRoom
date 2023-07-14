import sys
sys.setrecursionlimit(300000)

n, m, r = map(int, sys.stdin.readline().split())

visited = [True for _ in range(n+1)]
depth = [-1 for _ in range(n+1)]
adj = [[] for _ in range(n+1)]

def dfs(d, now):
    visited[now] = False
    depth[now] = d
    adj[now].sort(reverse=True)
    for next in adj[now]:
        if visited[next]:
            dfs(d+1, next)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)

dfs(0, r)

for result in range(1, n+1):
    print(depth[result])