import sys

while True:
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a == b == c == d == 0:
        break

    if a == b == c == d:
        print(0)
        continue

    cnt = 1

    while True:
        na = abs(a-b)
        nb = abs(b-c)
        nc = abs(c-d)
        nd = abs(d-a)

        if na == nb == nc == nd:
            break

        a, b, c, d = na, nb, nc, nd

        cnt += 1

    print(cnt)