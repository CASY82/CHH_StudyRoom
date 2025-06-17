import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    start = nums[0]
    tmp = 1
    res = 0

    for i in range(1, len(nums)):
        if nums[i] == start + 1:
            start = nums[i]
            tmp += 1
        else:
            res = max(res, tmp)
            tmp = 1
            start = nums[i]

    res = max(res, tmp)
    print(res)