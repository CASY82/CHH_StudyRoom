import sys

a, d, k = map(int, sys.stdin.readline().split())

if (k - a) % d != 0:
    print("X")
else:
    print(((k - a) // d) + 1)