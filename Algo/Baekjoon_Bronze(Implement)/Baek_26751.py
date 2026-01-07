# Najmniejsza liczba

import sys

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

if nums[0] == 0:
    if nums[1] == 0:
        nums[0], nums[2] = nums[2], nums[0]
    else:
        nums[0], nums[1] = nums[1], nums[0]

print("".join(map(str, nums)))