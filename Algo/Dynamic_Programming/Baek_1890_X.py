# 너무 아쉽게 틀림 거의 근접하였으나 자꾸 이상한데서 헤메고 있었다.
import sys

n = int(sys.stdin.readline())

game = []
dp = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    game.append(list(map(int, sys.stdin.readline().split())))

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        if i + game[i][j] < n:
            dp[i + game[i][j]][j] += dp[i][j]

        if j + game[i][j] < n:
            dp[i][j + game[i][j]] += dp[i][j]

print(dp[-1][-1])
