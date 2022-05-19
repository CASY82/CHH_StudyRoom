import sys

while True:
    try:
        a, b, c = map(int, sys.stdin.readline().split())
    except:
        break

    cnt = 0

    while a < b < c:
        if b - a <= c - b:
            a = b
            b = b + 1
        elif b - a > c - b:
            c = b
            b = b - 1

        cnt += 1

    print(cnt-1)