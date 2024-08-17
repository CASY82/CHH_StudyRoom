import sys

t = int(sys.stdin.readline())

for _ in range(t):
    g, c, e = map(int, sys.stdin.readline().split())

    if c < e:
        if g == 1:
            print(e - c)
        elif g == 2:
            print((e - c) * 3)
        elif g == 3:
            print((e - c) * 5)
    else:
        print(0)