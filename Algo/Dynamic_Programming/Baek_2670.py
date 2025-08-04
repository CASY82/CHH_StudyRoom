import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(float(sys.stdin.readline()))

dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(nums[i], dp[i - 1] * nums[i])

print(f"{max(dp):.3f}")