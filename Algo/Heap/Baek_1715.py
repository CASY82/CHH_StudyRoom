import sys
import heapq

n = int(sys.stdin.readline())
num = []
sum = 0

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

if len(num) == 1:
    print(0)
else:
    while len(num) > 1:
        a = heapq.heappop(num)
        b = heapq.heappop(num)
        heapq.heappush(num, a+b)
        sum += a+b

    print(sum)