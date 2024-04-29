import sys

p = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if p > c:
    print(50 * p - 10 * c + 500)
else:
    print(50 * p - 10 * c)