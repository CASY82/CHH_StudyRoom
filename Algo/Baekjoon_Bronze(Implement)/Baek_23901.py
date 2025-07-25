import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n = int(sys.stdin.readline())
    checkpoints = list(map(int, sys.stdin.readline().split()))
    res = 0

    for i in range(1, n - 1):
        if checkpoints[i] > checkpoints[i - 1] and checkpoints[i] > checkpoints[i + 1]:
            res += 1

    print("Case #{0}: {1}".format(case, res))