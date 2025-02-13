import sys

p = int(sys.stdin.readline())

for _ in range(p):
    k, n = map(int, sys.stdin.readline().split())

    # S1
    s1 = n * (n + 1) // 2

    # S2
    s2 = n * n

    # S3
    s3 = n * (n + 1)

    print("{0} {1} {2} {3}".format(k, s1, s2, s3))