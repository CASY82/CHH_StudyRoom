import sys
sys.setrecursionlimit(30000000)

n, m, r = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
depth = [-1] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    nodes[u].append(v)
    nodes[v].append(u)

index = [1]

def dfs(now, dep):
    if visited[now] == 0:
        visited[now] = index[0]
        depth[now] = dep
        index[0] += 1

        nodes[now].sort(reverse=True)

        for next in nodes[now]:
            dfs(next, dep + 1)

dfs(r, 0)

res = 0
for i in range(1, n + 1):
    res += visited[i] * depth[i]

print(res)