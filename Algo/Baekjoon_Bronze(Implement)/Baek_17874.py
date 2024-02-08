import sys

n, h, v = map(int, sys.stdin.readline().split())

print(max(n - h, h) * max(n - v, v) * 4)