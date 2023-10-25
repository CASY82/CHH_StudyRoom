import sys

t = int(sys.stdin.readline())

for _ in range(t):
    d, n, s, p = map(int, sys.stdin.readline().split())

    parallel = d + n * p
    serial = n * s

    if parallel > serial:
        print("do not parallelize")
    elif parallel == serial:
        print("does not matter")
    else:
        print("parallelize")