import sys
sys.setrecursionlimit(50000000)

n, m, r = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(n + 1)]
depth = [-1 for _ in range(n + 1)]
seq = [0 for _ in range(n + 1)]
res = 0
s = [1]

def dfs(now, dep):
    depth[now] = dep
    seq[now] = s[0]
    nodes[now].sort()
    for num in nodes[now]:
        if seq[num] == 0:
            s[0] += 1
            dfs(num, dep + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    nodes[u].append(v)
    nodes[v].append(u)

dfs(r, 0)

for i in range(1, n + 1):
    res += depth[i] * seq[i]

print(res)

# 다른 사람 풀이
# def dfs(x, depth):
#     global o
#     visited[x] = True
#     d[x] = depth
#     t[x] = o
#     o += 1
#     graph[x].sort()
#     for i in graph[x]:
#         if not visited[i]:
#             dfs(i, depth + 1)
#
# import sys
# sys.setrecursionlimit(150000)
# input = sys.stdin.readline
#
# N, M, R = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1)
# d = [-1] * (N + 1)
# t = [0] * (N + 1)
# o = 1
#
# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# dfs(R, 0)
#
# r = 0
# for i in range(1, N + 1):
#     r += d[i]*t[i]
# print(r)
