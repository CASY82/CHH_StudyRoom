import sys

n, w, h, l = map(int, sys.stdin.readline().split())

print(min((w // l) * (h // l), n))