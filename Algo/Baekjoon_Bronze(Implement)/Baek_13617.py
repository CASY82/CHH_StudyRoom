import sys

n, m = map(int, sys.stdin.readline().split())
res = 0

for _ in range(n):
    score = list(map(int, sys.stdin.readline().split()))

    if 0 not in score:
        res += 1

print(res)