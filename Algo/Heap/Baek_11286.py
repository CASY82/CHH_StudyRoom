import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            absol, tmp = heapq.heappop(heap)
            print(tmp)
        else:
            print(0)