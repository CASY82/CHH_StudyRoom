# 아 마이마이 하고 싶다
import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())
play_time = list(map(int, sys.stdin.readline().split()))

h = [0 for _ in range(m)]

for time in play_time:
    tmp = heapq.heappop(h)
    heapq.heappush(h, time + tmp)

res_check = heapq.heappop(h)

if res_check > k:
    print("GO")
else:
    print("WAIT")