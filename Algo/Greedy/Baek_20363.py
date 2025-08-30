import sys

x, y = map(int, sys.stdin.readline().split())

res = 0

res = x + y + min(x, y) // 10

print(res)