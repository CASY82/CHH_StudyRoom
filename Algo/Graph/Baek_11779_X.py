import sys
import heapq

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

city = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    src, dest, cost = map(int, sys.stdin.readline().split())
    city[src].append((dest, cost))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start):
    que = []

    heapq.heappush(que, (0, start))
    distance[start] = 0
    path = [-1 for _ in range(n + 1)]

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in city[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = now
                heapq.heappush(que, (cost, i[0]))

    return path

pathArray = dijkstra(start)
pathResult = [end]

temp = end
while pathArray[temp] != -1:
    pathResult.append(pathArray[temp])
    temp = pathArray[temp]

pathResult.reverse()

print(distance[end])
print(len(pathResult))
print(*pathResult)