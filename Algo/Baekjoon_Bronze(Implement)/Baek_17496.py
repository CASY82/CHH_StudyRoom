import sys

n, t, c, p = map(int, sys.stdin.readline().split())

can_grow = (n - 1) // t
print(can_grow * c * p)