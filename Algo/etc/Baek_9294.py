import sys
from itertools import combinations_with_replacement

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    res = []

    n, m, s = map(int, sys.stdin.readline().split())

    for comb in combinations_with_replacement(range(1, m + 1), n):
        if s == sum(comb):
            res.append(comb)

    print("Case {0}:".format(case))
    for i in res:
        print("(" + ",".join(map(str, i)) + ")")