import sys

t = int(sys.stdin.readline())

for _ in range(t):
    xm, ym, fm, xf, yf, ff = map(int, sys.stdin.readline().split())

    print(fm + ff + abs(xm - xf) + abs(ym - yf))