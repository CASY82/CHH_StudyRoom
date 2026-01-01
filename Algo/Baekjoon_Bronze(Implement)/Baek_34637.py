import sys

n, k = map(int, sys.stdin.readline().split())
level = set()

for _ in range(n):
    level.add(int(sys.stdin.readline()))

print(min(len(level), k))