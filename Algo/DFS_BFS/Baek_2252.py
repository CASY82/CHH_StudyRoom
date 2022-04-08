import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
tallest = [[] for i in range(n + 1)]
indegree = [0] * (n+1)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    tallest[a].append(b)
    indegree[b] += 1

def topology_sort():
    que = deque()
    visited = [True for _ in range(n + 1)]
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()

        for i in tallest[now]:
            indegree[i] -= 1
            if visited[i] and indegree[i] == 0:
                visited[i] = False
                que.append(i)

        if indegree[now] == 0:
            result.append(now)

    return result

print(*topology_sort())