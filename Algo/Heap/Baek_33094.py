import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())
days = list(map(int, sys.stdin.readline().split()))
tmp = []
res = 0

for i in range(n):
    heapq.heappush(tmp, -days[i])
    m -= days[i]

    if m < 0:
        if k > 0:
            k -= 1
            m += -heapq.heappop(tmp)
        else:
            break

    res += 1

print(res)