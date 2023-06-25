import sys

INF = int(1e9)
n, k = map(int, sys.stdin.readline().split())

coin = []
dp = [INF for _ in range(k+1)]
dp[0] = 0

for _ in range(n):
    val = int(sys.stdin.readline())
    coin.append(val)
    if val < k:
        dp[val] = 1

for i in range(1, k+1):
    for j in range(len(coin)):
        if i - coin[j] >= 0:
            if dp[i] > dp[i - coin[j]] + 1:
                dp[i] = dp[i - coin[j]] + 1

if dp[-1] < INF:
    print(dp[-1])
else:
    print(-1)