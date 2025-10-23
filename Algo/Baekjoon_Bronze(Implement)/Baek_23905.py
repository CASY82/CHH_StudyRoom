import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    point = 0
    res = 0

    res = 0
    point = 0

    for data in nums:
        expected = k - point

        if data == expected:
            point += 1
            if point == k:
                res += 1
                point = 0
        else:
            point = 1 if data == k else 0

    print("Case #{0}: {1}".format(case, res))