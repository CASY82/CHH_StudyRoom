import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    goals = int(sys.stdin.readline())

    dp = [0] * (goals+1)
    dp[0] = 1

    # 생각보다 간단했다... 2차원 배열로 접근했다가 결과가 안나오고 있었음
    # 1차원으로 접근해도 문제가 풀렸으며, 이에 따른 점화식도 굉장히 단순했다.
    for i in range(len(coins)):
        for j in range(coins[i], goals+1):
            dp[j] += dp[j - coins[i]]

    print(dp[goals])