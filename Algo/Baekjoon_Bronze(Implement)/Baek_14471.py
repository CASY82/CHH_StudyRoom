import sys

n, m = map(int, sys.stdin.readline().split())
result = []

for _ in range(m):
    correct, fail = map(int, sys.stdin.readline().split())

    if n-correct > 0:
        result.append(n-correct)

print(sum(result)-max(result))