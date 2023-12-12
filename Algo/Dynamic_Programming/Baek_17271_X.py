import sys

n, m = map(int, sys.stdin.readline().split())

dp = [1] * (n + 1)

if m > n:
    print(1)
else:
    for i in range(m, n + 1):
        dp[i] = (dp[i - 1] + dp[i - m]) % 1000000007

    print(dp[-1] % 1000000007)