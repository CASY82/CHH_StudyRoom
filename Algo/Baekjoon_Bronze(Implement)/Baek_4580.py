import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if nums[0] == 0:
        break

    tmp = nums[1:]
    res = []
    start = 0

    for i in range(1, len(tmp) + 1):
        for j in range(tmp[i - 1] - start):
            res.append(i)

        start = tmp[i - 1]

    print(*res)