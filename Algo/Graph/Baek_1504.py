import sys
import heapq

INF = int(1e9)

n, e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    que = []

    distance = [INF] * (n + 1)

    heapq.heappush(que, (0, start))
    distance[start] = 0

    if start == end:
        return 0

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

    return distance[end]

#이 부분을 약간 참고하게 되었으나 나머진 직접 생각함
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= int(1e9) or path2 >= int(1e9):
    print(-1)
else:
    print(min(path1, path2))