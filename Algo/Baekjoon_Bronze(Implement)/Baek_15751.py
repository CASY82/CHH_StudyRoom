import sys

a, b, x, y = map(int, sys.stdin.readline().split())

full_length = abs(b - a)
tele_length = abs(min(a, b)-min(x,y)) + abs(max(a,b)-max(x,y))

print(min(full_length, tele_length))