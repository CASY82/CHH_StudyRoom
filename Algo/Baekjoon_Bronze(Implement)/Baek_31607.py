import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if (a + b + c) - max(a, b, c) == max(a, b, c):
    print(1)
else:
    print(0)