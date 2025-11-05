import sys
import heapq

n, d = map(int, sys.stdin.readline().split())

monster = []
weapon = []
heapq.heapify(monster)
heapq.heapify(weapon)

res = 0

for _ in range(n):
    a, x = map(int, sys.stdin.readline().split())

    if a == 1:
        heapq.heappush(monster, x)
    else:
        heapq.heappush(weapon, x)

while True:
    if len(monster) > 0:
        mon = heapq.heappop(monster)

        if d > mon:
            d += mon
            res += 1
        else:
            while len(weapon) > 0:
                w = heapq.heappop(weapon)

                d *= w
                res += 1

                if d > mon:
                    d += mon
                    res += 1
                    break
            else:
                break
    else:
        res += len(weapon)
        break

print(res)