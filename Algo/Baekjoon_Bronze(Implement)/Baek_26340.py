import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h, w, c = map(int, sys.stdin.readline().split())
    origin_h = h
    origin_w = w

    for _ in range(c):
        if h > w:
            h //= 2
        else:
            w //= 2

    print("Data set: {0} {1} {2}".format(origin_h, origin_w, c))
    print(max(h, w), min(h, w))
    print()