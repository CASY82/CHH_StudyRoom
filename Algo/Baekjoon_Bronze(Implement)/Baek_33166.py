import sys

p, q = map(int, sys.stdin.readline().split())
a, b = map(int, sys.stdin.readline().split())

if p < q:
    print(p * a + (q - p) * b)
else:
    print(q * a)