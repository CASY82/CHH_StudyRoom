import sys

n = int(sys.stdin.readline())

monitors = []

for i in range(n):
    w, h = map(int, sys.stdin.readline().split())

    monitors.append((i + 1, w*w + h*h))

monitors.sort(key=lambda x : (-x[1], x[0]))

for i in range(n):
    print(monitors[i][0])