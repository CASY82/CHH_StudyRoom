import sys
import heapq

n, c = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))
res = [0 for _ in range(c)]

tmp = []
sangdamsa = 1

for i in range(c):
    if sangdamsa <= n:
        heapq.heappush(tmp, [times[i], sangdamsa])
        res[i] = sangdamsa
        sangdamsa += 1
    else:
        last_time, last_sangdamsa = heapq.heappop(tmp)
        for j in range(len(tmp)):
            tmp[j][0] -= last_time
        heapq.heappush(tmp, [times[i], last_sangdamsa])
        res[i] = last_sangdamsa

print(*res)