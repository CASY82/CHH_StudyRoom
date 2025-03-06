import sys

a, b, c = map(int, sys.stdin.readline().split())

if c % 2 == 1:
    print(a ^ b)
else:
    print(a)