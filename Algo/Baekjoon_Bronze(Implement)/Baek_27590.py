import sys

d_s, y_s = map(int, sys.stdin.readline().split())
d_m, y_m = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    if d_s % y_s == 0 and d_m % y_m == 0:
        print(cnt)
        break

    cnt += 1
    d_s += 1
    d_m += 1