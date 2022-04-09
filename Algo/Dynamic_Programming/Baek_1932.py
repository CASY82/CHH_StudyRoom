import sys

n = int(sys.stdin.readline())
triangle = []
dp = [[0] * (i+1) for i in range(n)]

for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))


dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            dp[i][j] = dp[i-1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
print(max(dp[-1]))