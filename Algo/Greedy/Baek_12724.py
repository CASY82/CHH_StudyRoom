import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n = int(sys.stdin.readline())

    x = list(map(int, sys.stdin.readline().split()))
    y = list(map(int, sys.stdin.readline().split()))

    x.sort()
    y.sort()
    res = 0

    for i in range(n):
        res += x[i] * y[n - 1 - i]

    print("Case #{0}: {1}".format(case, res))