import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    sticker = []

    for i in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if n >= 2:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i - 1] + sticker[0][i], dp[1][i - 2] + sticker[0][i], dp[0][i - 2] + sticker[0][i])
            dp[1][i] = max(dp[0][i - 1] + sticker[1][i], dp[0][i - 2] + sticker[1][i], dp[0][i - 2] + sticker[1][i])

    print(max(dp[0][-1], dp[1][-1]))