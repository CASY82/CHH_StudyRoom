import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

INF = 10 ** 15
ans = -INF

for top in range(n):
    tmp = [0] * m
    for bottom in range(top, n):
        for j in range(m):
            tmp[j] += a[bottom][j]

        cur = tmp[0]
        best = tmp[0]

        for j in range(1, m):
            cur = max(tmp[j], cur + tmp[j])
            best = max(best, cur)

        ans = max(ans, best)

print(ans)