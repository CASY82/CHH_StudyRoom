import sys

res = 0
n = int(sys.stdin.readline())
l = int(sys.stdin.readline())
potential = list(map(int, sys.stdin.readline().split()))

potential.sort(reverse=True)

for i in range(n):
    if potential[i] < 0 and l % 2 != 0:
        continue

    res += potential[i] ** l

print(res)