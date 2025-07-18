import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
gifts = list(map(int, sys.stdin.readline().split()))
child = list(map(int, sys.stdin.readline().split()))
res = True

tmp = []

for i in gifts:
    heapq.heappush(tmp, -i)

for want in child:
    tmp_box = -heapq.heappop(tmp)

    if want > tmp_box:
        res = False
        break
    else:
        tmp_box -= want
        heapq.heappush(tmp, -tmp_box)

if res:
    print(1)
else:
    print(0)