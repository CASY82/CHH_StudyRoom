# Outer Triangle Sum
import sys

case = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    total = 0

    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))

        if len(tmp) == 1:
            total += tmp[0]
        elif len(tmp) == n:
            total = total + sum(tmp)
        else:
            total = total + tmp[0] + tmp[-1]

    print("Case #{0}:{1}".format(case, total))
    case += 1