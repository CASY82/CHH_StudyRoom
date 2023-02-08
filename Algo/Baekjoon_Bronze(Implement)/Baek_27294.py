import sys

t, s = map(int, sys.stdin.readline().split())

if s == 0:
    if 12 <= t <= 16:
        print(320)
        exit()

print(280)