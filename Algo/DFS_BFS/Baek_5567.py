import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    src, dest = map(int, sys.stdin.readline().split())

    adj[src].append(dest)
    adj[dest].append(src)

def bfs(v):
    que = deque()
    que.append((v, 0))
    visited = [True for _ in range(n+1)]
    visited[v] = False
    cnt = 0

    while que:
        x, depth = que.popleft()

        if depth == 2:
            break

        for friend in adj[x]:
            if visited[friend]:
                que.append((friend, depth+1))
                visited[friend] = False
                cnt += 1

    return cnt

print(bfs(1))