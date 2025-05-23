import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    res = 0

    for i in range(n):
        name, cnt, cost = sys.stdin.readline().strip().split()

        cnt = int(cnt)
        cost = float(cost)

        res += cnt * cost

    print("${0:.2f}".format(res))