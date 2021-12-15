#약간의 힌트를 받고 푼 문제
import sys
t = int(sys.stdin.readline())
num = [0 for i in range(12)]

def dp(n):
    if n < 0:
        return 0

    if num[n] != 0:
        return num[n]

    if n <= 1:
        return 1

    if n >= 2:
        num[n] = dp(n-3) + dp(n-2) + dp(n-1)
        return dp(n-3) + dp(n-2) + dp(n-1)

for _ in range(t):
    n = int(sys.stdin.readline())

    print(dp(n))

#좀더 깔끔하게 정리된 코드
# T = int(input())
# input_list = []
#
# for i in range(T) :
#   input_list.append(int(input()))
#
# for t in input_list:
#   dp = [1,2,4]
#   for i in range(3, max(input_list)):
#     dp.append(dp[i-1] + dp[i-2] + dp[i-3])
#   print(dp[t-1])