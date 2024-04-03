import sys

n, m = map(int, sys.stdin.readline().split())

if m <= 100 * n:
    print("Yes")
else:
    print("No")
