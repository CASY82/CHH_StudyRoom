import sys

n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))

cost.sort()
max_cost = 0
res = 0
tmp = 0

for i in range(n):
    if tmp != cost[i]:
        tmp = cost[i]

        if max_cost < cost[i] * (n - i):
            max_cost = cost[i] * (n - i)
            res = cost[i]

print(max_cost, res)

# 다른 사람 풀이
# N = int(input())
# c = list(map(int, input().split()))
# c.sort()
# best_tuition = 0
# optimal_tuition = 100000000
# for i in range(N):
#     cost = c[i]
#     if cost*(N-i) > best_tuition:
#         best_tuition = cost*(N-i)
#         optimal_tuition = cost
# print(best_tuition, optimal_tuition)