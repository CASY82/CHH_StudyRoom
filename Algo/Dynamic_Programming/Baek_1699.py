# pypy로 통과함...
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
square_num = []


for i in range(1, n+1):
    if i * i <= n:
        dp[i * i] = 1
        square_num.append(i * i)

    for j in range(len(square_num)):
        if i - square_num[j] >= 0:
            if dp[i] > 0:
                if dp[i - square_num[j]] + 1 < dp[i]:
                    dp[i] = dp[i - square_num[j]] + 1
            else:
                dp[i] = dp[i - square_num[j]] + 1

print(dp[-1])

# 다른 사람 풀이 (python)
# import math
#
# N = int(input())
#
# dp = [0] * (N + 1)
# for i in range(1, N + 1):
#     dp[i] = i
#     for j in range(1, i):
#         if j * j > i:
#             break
#
#         if dp[i] > dp[i - j * j] + 1:
#             dp[i] = dp[i - j * j] + 1
# print(dp[N])
