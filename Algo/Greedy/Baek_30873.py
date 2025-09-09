import sys

n = int(sys.stdin.readline())
popularity = 0

for _ in range(n):
    p, c = map(int, sys.stdin.readline().split())

    if abs(p - popularity) <= c:
        popularity += 1

print(popularity)