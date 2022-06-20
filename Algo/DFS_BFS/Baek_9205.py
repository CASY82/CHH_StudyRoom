import sys
from collections import deque

t = int(sys.stdin.readline())

# 마지막 위치에 도달했으면 True반환 그렇지 못하면 False 반환

def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[0] = False

    while que:
        now_x, now_y = que.popleft()

        if now_x == location[-1][0] and now_y == location[-1][1]:
            return True

        for i in range(n+2):
            if visited[i]:
                if abs(now_x - location[i][0]) + abs(now_y - location[i][1]) <= 1000:
                    que.append((location[i][0], location[i][1]))
                    visited[i] = False

    return False


for _ in range(t):
    n = int(sys.stdin.readline())
    location = []
    visited = [True for i in range(n+2)]

    for _ in range(n + 2):
        location.append(list(map(int, sys.stdin.readline().split())))

    if bfs(location[0][0], location[0][1]):
        print("happy")
    else:
        print("sad")