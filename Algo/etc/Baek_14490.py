import sys

n, m = map(int, sys.stdin.readline().split(":"))

tmp = [0]

def Euclid(a, b):
    if a % b == 0:
        tmp[0] = b
    else:
        Euclid(b, a%b)

Euclid(n, m)

print("{0}:{1}".format(n // tmp[0], m // tmp[0]))