import sys
from collections import deque

n = int(sys.stdin.readline())
stone = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline())

def bfs(start):
    que = deque()
    que.append(start-1)

    visited = [0 for _ in range(n)]
    visited[start-1] = 1

    while que:
        now_stone = que.popleft()

        for i in (now_stone - stone[now_stone], now_stone + stone[now_stone]):
            if 0 <= i < n:
                if visited[i] == 0:
                    que.append(i)
                    visited[i] = 1

    result = visited.count(1)
    return result

print(bfs(start))