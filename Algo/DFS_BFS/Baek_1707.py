import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(n):
    que = deque()
    que.append(n)
    visited[n] = 1

    while que:
        now = que.popleft()

        for i in adj[now]:
            if visited[i] == 0:
                if visited[now] == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1

                que.append(i)
            else:
                if visited[now] == visited[i]:
                    return False

    return True


for _ in range(k):
    v, e = map(int, sys.stdin.readline().strip().split())

    adj = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v + 1)]
    result = []

    for _ in range(e):
        start, target = map(int, sys.stdin.readline().split())
        adj[start].append(target)
        adj[target].append(start)

    for i in range(1, v+1):
        if visited[i] == 0:
            if bfs(i):
                result.append(0)
            else:
                result.append(1)

    if sum(result) >= 1:
        print('NO')
    else:
        print('YES')