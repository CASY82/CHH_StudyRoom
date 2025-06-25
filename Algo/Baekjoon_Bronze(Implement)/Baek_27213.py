import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if m <= 2 or n <= 2:
    print(m * n)
else:
    print((m + n - 2) * 2)