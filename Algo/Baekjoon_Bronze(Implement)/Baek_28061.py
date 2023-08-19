import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    trees[i] -= (n + 1) - (i + 1)

print(max(trees))