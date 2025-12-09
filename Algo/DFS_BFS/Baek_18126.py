import sys
sys.setrecursionlimit(10**6)

N = int(input().strip())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B, C = map(int, input().split())
    adj[A].append((B, C))
    adj[B].append((A, C))

visited = [False] * (N + 1)
answer = 0

def dfs(node: int, dist: int):
    global answer
    visited[node] = True

    if dist > answer:
        answer = dist

    for nxt, cost in adj[node]:
        if not visited[nxt]:
            dfs(nxt, dist + cost)

dfs(1, 0)

print(answer)