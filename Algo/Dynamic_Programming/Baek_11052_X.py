# import sys
#
# n = int(sys.stdin.readline())
# card = [0] + list(map(int, sys.stdin.readline().split()))
# dp = [0 for _ in range(n+1)]
#
# dp[1] = card[1]
#
# for i in range(2, n):
#     for j in range(1, i+1):
#         dp[i] = max(dp[i-j] + card[j+1], dp[i])
#
# print(dp)

import sys

n = int(sys.stdin.readline())
card = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]

dp[1] = card[1]

# n 값을 기준으로 1개 짜리 일때 최댓값, 2개짜리 일때 최댓값...
# 위와 같이 각 단계에서 최댓값이 되는 경우를 구하는 것....
# 해당 최댓값을 다음 n값 에서 다시 활용함으로써 여러번 구할 필요가 없다.
for i in range(2, n + 1):
    for j in range(1, i+1):
        if dp[i] < dp[i - j] + card[j]:
            dp[i] = dp[i - j] + card[j]

print(dp[n])