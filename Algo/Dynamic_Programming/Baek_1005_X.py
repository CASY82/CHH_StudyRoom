import sys
from collections import deque

t = int(sys.stdin.readline())

def topology_sort(n, target, structureTime):
    result = [0] + structureTime
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        if now == target:
            return result

        for i in structureTree[now]:
            indegree[i] -= 1
            #DP일거 같았는데 정확한 식이 떠오르지 않아서 약간 참고함
            result[i] = max(result[now] + structureTime[i-1], result[i])
            if indegree[i] == 0:
                q.append(i)

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    structureTime = list(map(int, sys.stdin.readline().split()))
    indegree = [0] * (n + 1)
    structureTree = [[] for i in range(n + 1)]


    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        structureTree[x].append(y)
        indegree[y] += 1

    target = int(sys.stdin.readline())

    print(topology_sort(n, target, structureTime)[target])