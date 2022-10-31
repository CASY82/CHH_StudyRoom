import sys

n, k = map(int, sys.stdin.readline().split())
result = 0
last = 0

for _ in range(n):
    score = int(sys.stdin.readline())

    if score - last <= -k:
        result += 1

    last = score

print(result)