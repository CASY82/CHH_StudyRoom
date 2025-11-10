import sys

a = int(sys.stdin.readline())
w, v = map(int, sys.stdin.readline().split())

if a <= w // v:
    print(1)
else:
    print(0)