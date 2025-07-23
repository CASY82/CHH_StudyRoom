import sys
import heapq

t = int(sys.stdin.readline())
MOD = 10 ** 9 + 7

for _ in range(t):
    n = int(sys.stdin.readline())
    slime = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(slime)
    cost = 1

    while len(slime) > 1:
        a = heapq.heappop(slime)
        b = heapq.heappop(slime)

        step = a * b
        cost = cost * (step % MOD) % MOD
        heapq.heappush(slime, step)

    print(cost)