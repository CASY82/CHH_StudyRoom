# The Merchant of Venice

import sys

k = int(sys.stdin.readline())

for case in range(1, k + 1):
    n, s, d = map(int, sys.stdin.readline().split())

    res = 0

    for i in range(n):
        di, vi = map(int, sys.stdin.readline().split())

        if di <= s * d:
            res += vi

    print(f"Data Set {case}:")
    print(res)
    print()