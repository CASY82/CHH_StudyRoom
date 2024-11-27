import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n, b = map(int, sys.stdin.readline().split())
    houses = list(map(int, sys.stdin.readline().split()))
    res = 0

    houses.sort()

    for cost in houses:
        if b - cost >= 0:
            b -= cost
            res += 1
        else:
            break

    print("Case #{0}: {1}".format(case, res))