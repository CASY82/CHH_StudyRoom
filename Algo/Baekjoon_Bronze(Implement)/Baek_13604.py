import sys

j, r = map(int, sys.stdin.readline().split())
rounds = list(map(int, sys.stdin.readline().split()))

player = [0] * j

for i in range(j * r):
    player[i % j] += rounds[i]

max_score = max(player)
result = 1

for k in range(j):
    if player[result - 1] <= player[k]:
        result = k + 1

print(result)