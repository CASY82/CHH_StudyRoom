import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n, p, q = map(int, sys.stdin.readline().split())
    eggs = list(map(int, sys.stdin.readline().split()))

    res = 0
    weight = 0
    eggs.sort()

    for i in range(len(eggs)):
        if res < p:
            if weight + eggs[i] <= q:
                res += 1
                weight += eggs[i]
            else:
                break
        else:
            break

    print("Case {0}: {1}".format(case, res))