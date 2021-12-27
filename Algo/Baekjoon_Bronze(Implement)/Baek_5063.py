import sys

n = int(sys.stdin.readline())

for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().split())

    ad = e - c

    if r > ad:
        print("do not advertise")
    elif r < ad:
        print("advertise")
    else:
        print("does not matter")