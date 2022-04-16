import sys

n = int(sys.stdin.readline())

consulting = []
dp = [0 for _ in range(n+1)]

for i in range(n):
    consulting.append(list(map(int, sys.stdin.readline().split())))
    dp[i] = consulting[i][1]

for i in range(n-1, -1, -1):
    if i + consulting[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        # 즉 경우에 따라나눠지는게 아니라 뒤에서 부터 그냥 최댓값을 계속 끌고가는 형태
        dp[i] = max(dp[i+1], consulting[i][1] + dp[i + consulting[i][0]])

print(dp[0])