import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    tmp = n - m

    if tmp % 2 == 0:
        print(tmp // 2, 0)
    else:
        if tmp == 1:
            print(0, 0)
        else:
            print(tmp // 2 - 1, 1)