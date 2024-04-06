import sys

a, b = map(int, sys.stdin.readline().split())

if a <= b:
    print(a + (a - 1))
else:
    print(b + (b + 1))