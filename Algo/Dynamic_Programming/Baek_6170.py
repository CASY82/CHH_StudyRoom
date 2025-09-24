import sys

case = int(sys.stdin.readline())
tmp = []

for _ in range(case):
    n = int(sys.stdin.readline())
    tmp.append(n)

max_n = max(tmp)

dp = [0] * (max_n + 2)

if max_n >= 1:
    dp[1] = 2

if max_n >= 2:
    dp[2] = 3

for i in range(3, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

for ca, m in enumerate(tmp, 1):
    print("Scenario #{}:".format(ca))
    print(dp[m])
    print()