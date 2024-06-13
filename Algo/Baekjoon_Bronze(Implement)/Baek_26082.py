import sys

a, b, c = map(int, sys.stdin.readline().split())

print(b // a * c * 3)