import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
visited = [True for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    A_i, B_i = map(int, sys.stdin.readline().split())

    adj[A_i].append(B_i)
    adj[B_i].append(A_i)

#시작은 1부터 해서 거리가 같은 노드를 찾는다.
def bfs():
    que = deque()
    que.append((1, 0))
    visited[1] = False

    while que:
        now, dist = que.popleft()

        result[now] = dist

        for i in adj[now]:
            if visited[i]:
                visited[i] = False
                que.append((i, dist+1))

bfs()

#이제 result에서 max값을 가진 애들만 뽑아 준다.
max_val = max(result)
answer = [i for i, v in enumerate(result) if max_val == v]

print(answer[0], max_val, len(answer))