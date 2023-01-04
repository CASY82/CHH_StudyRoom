import sys
from collections import deque

a, b, n, m = map(int, sys.stdin.readline().split())

visited = [True for _ in range(100001)]

def bfs(start, end, a, b):
    que = deque()
    que.append((start, 0))
    visited[start] = False

    while que:
        now, cnt = que.popleft()

        if now == end:
            return cnt

        for nxt in (1, -1, a, b, -a, -b):
            tmp = now + nxt
            if 0 <= tmp <= 100000:
                if visited[tmp]:
                    visited[tmp] = False
                    que.append((tmp, cnt + 1))

        for nxt in (a, b):
            tmp = now * nxt
            if 0 <= tmp <= 100000:
                if visited[tmp]:
                    visited[tmp] = False
                    que.append((tmp, cnt + 1))

print(bfs(n, m, a, b))