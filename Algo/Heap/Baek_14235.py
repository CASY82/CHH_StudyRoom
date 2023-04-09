import sys
import heapq

n = int(sys.stdin.readline())
gift = []

for _ in range(n):
    action = list(map(int, sys.stdin.readline().split()))

    if action[0] == 0:
        if gift:
            print(-heapq.heappop(gift))
        else:
            print(-1)
            continue
    else:
        for giftnum in range(1, len(action)):
            heapq.heappush(gift, -action[giftnum])