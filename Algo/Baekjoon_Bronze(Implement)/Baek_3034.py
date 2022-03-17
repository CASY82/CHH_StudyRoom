import sys

n, w, h = map(int, sys.stdin.readline().split())

max_length = int((w*w + h*h) ** 0.5)

cnt = 0

for _ in range(n):
    matches = int(sys.stdin.readline())

    if matches <= max_length:
        print("DA")
    else:
        print("NE")