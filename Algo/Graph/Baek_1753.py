# 기존의 For문으로 푸는 방법(n^2 : 시간 초과)

# import sys
# INF = int(1e9)
# 
# v, e = map(int, sys.stdin.readline().split())
# 
# k = int(sys.stdin.readline())
# 
# graph = [[]for _ in range(v + 1)]
# visited = [False] * (v + 1)
# distance = [INF] * (v + 1)
# 
# for _ in range(e):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a].append((b, c))
# 
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, v + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
# 
#     return index
# 
# def dijkstra(k):
#     distance[k] = 0
#     visited[k] = True
#     for j in graph[k]:
#         distance[j[0]] = j[1]
# 
#     for i in range(v - 1):
#         now = get_smallest_node()
#         visited[now] = True
# 
#         for j in graph[now]:
#             cost = distance[now] + j[1]
# 
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# 
# dijkstra(k)
# 
# for i in range(1, v + 1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

# 우선 순위 큐를 이용한 방법(ElogV)

import heapq
import sys

INF = int(1e9)

v, e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(v+1)]

k = int(sys.stdin.readline())
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def dijkstra(k):
    q = []
    heapq.heappush(q, (0, k))
    distance[k] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])