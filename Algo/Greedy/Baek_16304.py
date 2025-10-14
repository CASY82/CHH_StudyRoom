import sys

n, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

res = 1

for i in range(1, n):
    if nums[i - 1] + nums[i] <= x:
        res = i + 1

print(res)