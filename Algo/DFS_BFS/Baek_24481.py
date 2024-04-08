import sys
sys.setrecursionlimit(1000000)

n, m, r = map(int, sys.stdin.readline().split())
visited = [-1] * (n + 1)
graph = [[] for _ in range(n + 1)]
check = 0

def dfs(now, check):
    if visited[now] == -1:
        visited[now] = check
        for node in graph[now]:
            dfs(node, check + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

dfs(r, 0)

for i in range(1, len(visited)):
    print(visited[i])

# 다른 사람 풀이
# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
#
# n, m, r = map(int, input().split())
# graph = defaultdict(list)
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# for k, v in graph.items():
#     graph[k] = sorted(graph[k])
#
# def dfs(x, depth):
#     answer[x] = depth
#
#     for neib in graph[x]:
#         if answer[neib] == -1:
#             dfs(neib, depth+1)
#
# answer = {x:-1 for x in range(1, n+1)}
#
# answer[r] = 0
# dfs(r, 0)
#
# for k, v in answer.items():
#     print(v)