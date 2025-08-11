import sys
import heapq

n = int(sys.stdin.readline())

problem = []

for _ in range(n):
    deadline, ramen = map(int, sys.stdin.readline().split())
    problem.append((deadline, ramen))

problem.sort(key=lambda x:x[0])

min_heap = []

for d, r in problem:
    heapq.heappush(min_heap, r)

    if len(min_heap) > d:
        heapq.heappop(min_heap)

print(sum(min_heap))