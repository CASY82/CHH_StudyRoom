import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0 and len(heap) == 0:
        print(0)
        continue

    elif num == 0:
        print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, num)