import sys
from collections import deque

n = int(sys.stdin.readline())

jump = list(map(int, sys.stdin.readline().split()))

visited = [True for _ in range(n)]

def bfs():
    que = deque()
    que.append((0, 0))
    visited[0] = False

    while que:
        loc, cnt = que.popleft()

        if loc == n-1:
            return cnt

        for i in range(1, jump[loc]+1):
            if loc + i >= n:
                continue
            if visited[loc + i]:
                visited[loc + i] = False
                que.append((loc + i, cnt + 1))

    return -1

result = bfs()

print(result)