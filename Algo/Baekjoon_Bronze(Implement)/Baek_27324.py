import sys

n = int(sys.stdin.readline())

if n % 10 == n // 10:
    print(1)
else:
    print(0)