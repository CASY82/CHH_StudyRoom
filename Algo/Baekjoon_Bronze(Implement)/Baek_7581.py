import sys

while True:
    l, w, h, v = map(int, sys.stdin.readline().split())

    if l == w == h == v == 0:
        break

    if v == 0:
        v = l * w * h
    else:
        if l == 0:
            l = v // (w * h)
        elif w == 0:
            w = v // (h * l)
        elif h == 0:
            h = v // (l * w)

    print(l, w, h, v)