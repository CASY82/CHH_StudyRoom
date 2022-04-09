import sys

n = int(sys.stdin.readline())
stair = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    stair[i] = (int(sys.stdin.readline()))

dp[0] = stair[0]
dp[1] = max(stair[1] + stair[0], stair[1])
dp[2] = max(stair[2] + stair[0], stair[2] + stair[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[n-1])