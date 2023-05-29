import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(10):
    dp[0][i] = 1

for j in range(n):
    if j > 0:
        for k in range(10):
            if k == 0:
                dp[j][k] = dp[0][0]
            else:
                dp[j][k] = dp[j-1][k] + dp[j][k-1]

print(sum(dp[n-1]) % 10007)