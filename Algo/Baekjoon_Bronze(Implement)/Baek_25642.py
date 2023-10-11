import sys

yt, yj = map(int, sys.stdin.readline().split())

while True:
    yj += yt

    if yj >= 5:
        print("yt")
        break

    yt += yj

    if yt >= 5:
        print("yj")
        break