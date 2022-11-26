import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(first, n):
    que = deque()
    que.append((first, 0))

    while que:
        now, cnt = que.popleft()

        if now == n:
            return cnt

        if visited[now]:
            visited[now] = False
            que.append((player[now], cnt+1))

    return 0

for _ in range(t):
    n = int(sys.stdin.readline())

    player = [0 for _ in range(n+1)]
    visited = [True for _ in range(n + 1)]

    for i in range(1, n+1):
        choose = int(sys.stdin.readline())
        player[i] = choose

    print(bfs(1, n))