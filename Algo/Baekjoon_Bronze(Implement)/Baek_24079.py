import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())

if (x + y) * 60 > z * 60 + 30:
    print(0)
else:
    print(1)
