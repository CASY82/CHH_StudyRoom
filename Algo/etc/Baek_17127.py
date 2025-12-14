import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))

prod = [[1]*n for _ in range(n)]
for l in range(n):
    p = 1
    for r in range(l, n):
        p *= tree[r]
        prod[l][r] = p

ans = 0
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            s = (
                prod[0][i] +
                prod[i + 1][j] +
                prod[j + 1][k] +
                prod[k + 1][n - 1]
            )
            if s > ans:
                ans = s

print(ans)