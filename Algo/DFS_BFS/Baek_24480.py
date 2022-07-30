import sys
sys.setrecursionlimit(300000)

n, m, r = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
visited = [True for _ in range(n+1)]
result = [0 for _ in range(n)]
cnt = [1]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)

def dfs(r):
    visited[r] = False
    result[r - 1] = cnt[0]
    cnt[0] += 1
    tmp = adj[r]
    tmp.sort(reverse=True)

    for i in tmp:
        if visited[i]:
            dfs(i)

dfs(r)

for j in result:
    print(j)