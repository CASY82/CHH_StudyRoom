import sys

n = int(sys.stdin.readline())
expensive_loc = 0
jinju_cost = 0
costs = []

for _ in range(n):
    loc, cost = sys.stdin.readline().strip().split()

    cost = int(cost)

    if loc == "jinju":
        jinju_cost = cost

    costs.append(cost)

for i in range(n):
    if costs[i] > jinju_cost:
        expensive_loc += 1

print(jinju_cost)
print(expensive_loc)