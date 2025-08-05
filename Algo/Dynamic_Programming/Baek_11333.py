MOD = 1_000_000_007
MAX_N = 10000

dp = [0] * (MAX_N + 1)
dp[0] = 1
dp[3] = 3

for i in range(6, MAX_N + 1, 3):
    dp[i] = dp[i - 3] * 3 % MOD
    for j in range(6, i + 1, 3):
        dp[i] = (dp[i] + dp[i - j] * (j * 2 // 3)) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
