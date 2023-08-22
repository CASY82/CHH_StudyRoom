import sys

uk, jae = map(int, sys.stdin.readline().split())

m = (jae - uk) / 400
value = 1 / (1 + (10 ** m))

print(value)