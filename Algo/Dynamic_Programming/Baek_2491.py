import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

dp = [1 for i in range(n)]
dp2 = [1 for i in range(n)]

for i in range(1, n):
    if number[i-1] <= number[i]:
        dp[i] = dp[i-1] + 1

for i in range(n-1, 0, -1):
    if number[i] <= number[i-1]:
        dp2[i-1] = dp2[i] + 1

print(max(max(dp), max(dp2)))