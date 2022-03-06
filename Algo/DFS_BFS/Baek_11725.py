# 나는 bfs로 풀었다.
import sys
from collections import deque

n = int(sys.stdin.readline())
adj = [[] for i in range(n + 1)]
visited = [0, 1] + [0] * (n-1)

for i in range(n-1):
    src, dest = map(int, sys.stdin.readline().split())

    adj[src].append(dest)
    adj[dest].append(src)

def bfs(x):
    que = deque()
    que.append(x)

    while que:
        num = que.popleft()

        for next in adj[num]:
            if visited[next] == 0:
                if next != num:
                    que.append(next)
                    visited[next] = num

bfs(1)

for i in range(2, n+1):
    print(visited[i])

#dfs 풀이 참고
#
# from collections import deque
# import sys
#
# def DFS(i):
#     global visited
#     stack.append(i)
#     while stack:
#         a = stack.pop()
#         for i in graph[a]:
#             if not visited[i]:
#                 visited[i] = a
#                 stack.append(i)
#
# n = int(sys.stdin.readline().strip())
# graph = [[] for i in range(n + 1)]
#
# for i in range(n - 1):
#     a, b = map(int, sys.stdin.readline().strip().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# stack = deque()
# visited = [False] * (n + 1)
# DFS(1) # 시작 노드 "1"
# for i in range(2, n + 1):
#     print(visited[i])

# 다른 dfs 풀이
# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
#
# def input():
#     return sys.stdin.readline().rstrip()
#
#
# N = int(input())
# graph = [[0] for _ in range(N + 1)]
# visited = [False] * (N + 1)
# answer = []
#
# for _ in range(1, N):
#     k, v = map(int, input().split())
#     graph[k].append(v)
#     graph[v].append(k)
#
#
# def dfs(cur, parent):
#     if not visited[cur]:
#         visited[cur] = True
#         answer.append([cur, parent])
#         for node in graph[cur]:
#             dfs(node, cur)
#
#
# dfs(1, 1)
#
# answer = answer[2:]
# answer.sort()
# for item in answer:
#     print(item[1])