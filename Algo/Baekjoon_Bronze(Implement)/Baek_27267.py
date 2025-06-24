import sys

a, b, c, d = map(int, sys.stdin.readline().split())

m = a * b
p = c * d

if m > p:
    print("M")
elif m < p:
    print("P")
else:
    print("E")