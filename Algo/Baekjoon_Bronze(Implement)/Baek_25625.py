import sys

x, y = map(int, sys.stdin.readline().split())

if x <= y:
    print(y - x)
else:
    print(x + y)