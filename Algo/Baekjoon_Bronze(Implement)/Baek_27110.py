import sys

n = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())

print(min(n, a) + min(b, n) + min(c, n))