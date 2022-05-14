import sys
sys.setrecursionlimit(300000)

n, m, r = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]

visited = [0 for _ in range(n+1)]
cnt = [0]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)

for i in range(len(adj)):
    adj[i].sort()

def dfs(now):
    if visited[now] == 0:
        cnt[0] += 1
        visited[now] = cnt[0]

        for i in adj[now]:
            dfs(i)

dfs(r)

for i in range(1, n+1):
    print(visited[i])