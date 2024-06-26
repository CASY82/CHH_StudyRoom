import sys

n, d = map(int, sys.stdin.readline().split())
solve = []

for _ in range(n):
    solve.append(int(sys.stdin.readline()))

total = sum(solve)
reward_min = d // total

for i in range(n):
    print(solve[i] * reward_min)