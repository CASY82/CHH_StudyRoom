import sys

n = int(sys.stdin.readline())

for _ in range(n):
    k, p, x = map(int, sys.stdin.readline().split())

    res = 9999999999999999999

    for i in range(1, 10001):
        now_cost = k / i * p + i * x

        res = min(res, now_cost)

    print("{:.3f}".format(res))