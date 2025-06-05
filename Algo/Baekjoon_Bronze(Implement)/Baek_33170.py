import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b + c <= 21:
    print(1)
else:
    print(0)