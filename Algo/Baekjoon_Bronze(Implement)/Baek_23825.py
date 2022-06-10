import sys

s, a = map(int, sys.stdin.readline().split())

print(min(s // 2, a // 2))