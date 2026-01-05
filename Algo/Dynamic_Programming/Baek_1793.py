# 타일링

import sys

nums = [int(line.strip()) for line in sys.stdin if line.strip()]
if not nums:
    sys.exit(0)

max_n = max(nums)

dp = [0] * (max_n + 1)

dp[0] = 1 # 아무것도 못함 1가지
if max_n >= 1:
    dp[1] = 1 # 세로로 세운 벽돌 1개

# case A : 마지막에 세로 하나 세움 dp[n - 1]
# case B : 마지막에 2 x 1 두개를 포개서 2 x 2를 한개 만든다 dp[n - 2]
# case C : 마지막에 2 x 2 한개를 둔다 dp[n - 2]
# 결과적으로 (dp[n - 1] + dp[n - 2] * 2)

for n in range(2, max_n + 1):
    dp[n] = dp[n - 1] + dp[n - 2] * 2

for res_n in nums:
    print(dp[res_n])
