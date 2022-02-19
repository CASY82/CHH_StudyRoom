import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

heapq.heapify(card)

for i in range(m):
    tmp = heapq.heappop(card) + heapq.heappop(card)
    heapq.heappush(card, tmp)
    heapq.heappush(card, tmp)

print(sum(card))