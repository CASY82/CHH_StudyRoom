import sys

n, m = map(int, sys.stdin.readline().split())

book = [[]]
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for _ in range(m):
    days, page = map(int, sys.stdin.readline().split())

    book.append([days, page])

for i in range(1, m + 1):
    for j in range(n + 1):
        if j - book[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j - book[i][0]] + book[i][1], dp[i - 1][j])
        dp[i][j] = max(dp[i - 1][j], dp[i][j])

print(dp[m][n])