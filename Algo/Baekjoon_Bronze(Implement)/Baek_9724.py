import sys

t = int(sys.stdin.readline())

for case in range(t):
    a, b = map(int, sys.stdin.readline().split())
    cnt = 0

    i = 1

    while i ** 3 <= 2000000000:
        if a <= i ** 3 <= b:
            cnt += 1

        i += 1

    print("Case #{0}: {1}".format(case + 1, cnt))