import sys

n, t = map(int, sys.stdin.readline().split())
dp = [0] * (t + 1)

for _ in range(n):
    k, s = map(int, sys.stdin.readline().split())

    for st in range(t, k - 1, -1):
        dp[st] = max(dp[st], dp[st - k] + s)

print(max(dp))