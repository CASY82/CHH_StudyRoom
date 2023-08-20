import sys

n = int(sys.stdin.readline())

# 짝수에서만 만들 수 있음(높이가 3이므로)
dp = [0] * 31
dp[2] = 3

#모양이 총 3분류가 있음 (가로 2줄, 4줄, 6줄)
# 2줄 3
# 4줄 11
# 6줄 2 (고정)
if n % 2 == 1:
    print(0)
else:
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * dp[2] + sum(dp[:i-2])*2 + 2

    print(dp[n])