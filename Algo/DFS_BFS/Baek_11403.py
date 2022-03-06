import sys
from collections import deque

n = int(sys.stdin.readline())
nodeGraph = []
adj = [[0 for i in range(n)] for j in range(n)]

for _ in range(n):
    nodeGraph.append(list(map(int, sys.stdin.readline().split())))

#방향이 있으므로 가면 못돌아옴. visited가 필요 BFS,DFS 둘다 가능하긴할듯
def bfs(v):
    que = deque()
    que.append(v)
    visited = [True for _ in range(n)]

    while que:
        node = que.popleft()

        for i in range(len(nodeGraph[node])):
            if nodeGraph[node][i] == 1:
                if visited[i]:
                    que.append(i)
                    adj[v][i] = 1
                    visited[i] = False

for i in range(n):
    bfs(i)

for i in range(n):
    print(*adj[i])