# Arithmetic and Geometric Sums
import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    nums = list(map(int, sys.stdin.readline().split()))
    res = 0

    if 0 not in nums and len((set(nums))) > 1:
        if nums[1] / nums[0] == nums[2] / nums[1]:
            res = nums[0] * ((nums[1] / nums[0]) ** n - 1) / ((nums[1] / nums[0]) - 1)
        elif nums[1] - nums[0] == nums[2] - nums[1]:
            res = n * (2 * nums[0] + (n - 1) * (nums[1] - nums[0])) / 2
    elif nums[1] - nums[0] == nums[2] - nums[1]:
        res = n * (2 * nums[0] + (n - 1) * (nums[1] - nums[0])) / 2

    print(int(res))