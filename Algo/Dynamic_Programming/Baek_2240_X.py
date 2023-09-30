import sys

t, w = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(w+1)] for _ in range(t)]

# 시간을 센다.
for i in range(t):
    tree = int(sys.stdin.readline())

    # 1번 위치면, 0위치는 자연스럽게 tree == 1인 경우에만 수가 올라간다.
    if tree == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    # 여기서는 위치를 변경한다.
    for j in range(1, w+1):
        # 1번 나무는 w가 짝수인 경우에 +1 / 2번 나무는 w가 홀수인 경우에 +1
        if (tree == 2 and j % 2 == 1) or (tree == 1 and j % 2 == 0):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))