import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(start, end, path ,visited):
    que = deque()
    que.append(path[start-1])
    visited[start-1] = False
    cnt = 0

    while que:
        tmp = que.popleft()

        for v in tmp:
            if visited[v-1]:
                cnt += 1
                visited[v-1] = False
                que.append(path[v-1])
    return cnt


for _ in range(t):
    nation, airplane = map(int, sys.stdin.readline().split())

    airplane_path = [[] for _ in range(nation)]

    for _ in range(airplane):
        src, dest = map(int, sys.stdin.readline().split())

        airplane_path[src - 1].append(dest)
        airplane_path[dest - 1].append(src)

    visited = [True] * nation

    result = bfs(1, airplane, airplane_path, visited)

    print(result)

#놀랍게도 정답은 그냥 n-1이라 한다... 그래도 장하다 난 bfs로 결국 풀어내었다.