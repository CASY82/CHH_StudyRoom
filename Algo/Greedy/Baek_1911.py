import sys

n, l = map(int, sys.stdin.readline().split())
puddles = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
puddles.sort()

covered = 0
res = 0

for s, e in puddles:
    start = max(s, covered)

    if start >= e:
        continue

    need = e - start
    k = (need + l - 1) // l
    res += k
    covered = start + k * l

print(res)