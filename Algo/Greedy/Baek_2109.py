# 순회 강연
import sys
import heapq

n = int(sys.stdin.readline())
lectures = []

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    lectures.append((d, p))

lectures.sort()  # 마감일 오름차순

heap = []

for d, p in lectures:
    heapq.heappush(heap, p)

    # d일까지 가능한 강연 수는 최대 d개
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))