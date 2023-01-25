import sys

t = int(sys.stdin.readline())

dp = [1 for _ in range(10001)]

# 2를 선택하는 경우를 이전 dp값에서 하나씩 더해온다.
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 3을 선택하는 경우를 이전 dp값에서 하나씩 더해온다.
for j in range(3, 10001):
    dp[j] += dp[j - 3]

for _ in range(t):
    num = int(sys.stdin.readline())

    print(dp[num])