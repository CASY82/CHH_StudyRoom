import sys
from collections import deque

n = int(sys.stdin.readline())
starter, targeter = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
arr_list = [[] for _ in range(n+1)]

for _ in range(m):
    src, dest = map(int, sys.stdin.readline().split())

    arr_list[src].append(dest)
    arr_list[dest].append(src)

cnt = 0
queue = deque([(starter, cnt)])
result = -1
visited = [False for _ in range(n+1)]

while queue:
    st, cnt = queue.popleft()
    visited[st] = True

    if targeter == st:
        result = cnt
        break

    for i in arr_list[st]:
        if not visited[i]:
            queue.append((i, cnt + 1))

print(result)