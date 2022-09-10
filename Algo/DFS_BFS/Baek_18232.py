import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
telelport = [[] for _ in range(n+1)]
visisted = [True for _ in range(n+1)]

time = [int(1e9) for _ in range(n+1)]

for _ in range(m):
    src, dest = map(int, sys.stdin.readline().split())
    telelport[src].append(dest)
    telelport[dest].append(src)

def bfs(s, e):
    que = deque()
    time[s] = 0
    que.append(s)
    visisted[s] = False


    while que:
        now = que.popleft()

        if now == e:
            return time[now]

        for loc in telelport[now]:
            if visisted[loc] and (time[loc] > time[now] + 1):
                que.append(loc)
                visisted[loc] = True
                time[loc] = time[now] + 1

        for next in (now + 1, now - 1):
            if (1 <= next <= n) and (time[next] > time[now] + 1):
                if visisted[next]:
                    que.append(next)
                    visisted[next] = True
                    time[next] = time[now] + 1

print(bfs(s, e))