import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    a, d, g = map(int, sys.stdin.readline().split())

    score = a * (d + g)

    if a == (d + g):
        score *= 2

    result = max(result, score)

print(result)