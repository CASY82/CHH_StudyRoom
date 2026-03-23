# 불안정한 수열
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

res = 0

for i in range(1, n):
    if nums[i] % 2 != nums[i - 1] % 2:
        res += 1

print(res + 1)