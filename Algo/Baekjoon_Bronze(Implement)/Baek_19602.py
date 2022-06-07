import sys

s = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = int(sys.stdin.readline())

if 1 * s + 2 * m + 3 * l < 10:
    print("sad")
else:
    print("happy")