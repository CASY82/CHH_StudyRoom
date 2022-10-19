import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

c *= 2
if c > a + b:
    print(a+b)
else:
    print(a+b-c)