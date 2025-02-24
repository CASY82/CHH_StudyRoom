import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
queue = deque([1])
visited[1] = 1
check = True

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    nodes[v].append(u)
    nodes[u].append(v)

while queue:
    now = queue.popleft()

    for v in nodes[now]:
        if visited[v] == 0:
            queue.append(v)
            visited[v] = 1

for i in range(1, n + 1):
    if visited[i] == 0:
        check = False
        print(i)

if check:
    print(0)

# 다른 사람 풀이

# n, m = map(int, input().split())
#
# cow = [[] for _ in range(n + 1)]
# cow[0] = [1]
#
# for i in range(m):
#     x, y = map(int, input().split())
#     cow[x].append(y)
#     cow[y].append(x)
#
# rel = [1] + [0] * n
#
# stack = [0]
# while stack:
#     a = stack.pop()
#     for i in cow[a]:
#         if not rel[i]:
#             rel[i] = 1
#             stack.append(i)
# if 0 in rel:
#     for i in range(1, n + 1):
#         if rel[i] == 0:
#             print(i)
# else:
#     print(0)