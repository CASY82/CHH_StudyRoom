import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    s1 = n * (n + 1) // 2
    s2 = n ** 2
    s3 = n * (n + 1)

    print(s1, s2, s3)