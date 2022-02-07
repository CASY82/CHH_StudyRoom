import sys
sys.setrecursionlimit(10 ** 5)

n, m, k = map(int, sys.stdin.readline().split())
cnt = 0

passage = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x, y, n, m):
    cntF = 0

    if x >= m or y >= n or x < 0 or y < 0:
        return 0

    if passage[y][x] == 1:
        passage[y][x] = 0
        a = dfs(x - 1, y, n, m)
        b = dfs(x, y - 1, n, m)
        c = dfs(x, y + 1, n, m)
        d = dfs(x + 1, y, n, m)
        cntF = 1 + a + b + c + d

    return cntF

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())

    passage[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        tmp = dfs(j, i, n, m)
        if tmp > cnt:
            cnt = tmp

print(cnt)