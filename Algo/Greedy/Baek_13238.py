import sys

n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))

max_cost = coin[0]
min_cost = coin[0]
max_diff = 0

for i in range(1, n):
    if min_cost > coin[i]:
        min_cost = coin[i]
        max_cost = coin[i]

    max_cost = max(coin[i], max_cost)
    max_diff = max(max_cost - min_cost, max_diff)

print(max_diff)