import sys

n, s = map(int, sys.stdin.readline().split())
problems = []

for _ in range(n):
    low, high = map(int, sys.stdin.readline().split())

    problems.append((low, high))

# problems.sort()

for low, high in problems:
    if low <= s <= high:
        s += 1

print(s)