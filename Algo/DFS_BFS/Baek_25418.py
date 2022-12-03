import sys
from collections import deque

history = set()

def bfs(start, end):
    que = deque()
    que.append((start, 0))
    history.add(start)

    while que:
        now, cnt = que.popleft()

        if now == end:
            return cnt

        if now * 2 not in history and now * 2 <= end:
            que.append((now * 2, cnt + 1))
            history.add(now * 2)

        if now + 1 not in history and now + 1 <= end:
            que.append((now + 1, cnt + 1))
            history.add(now + 1)



a, k = map(int, sys.stdin.readline().split())

print(bfs(a, k))