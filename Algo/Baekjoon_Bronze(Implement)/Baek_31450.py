import sys

m, k = map(int, sys.stdin.readline().split())

if m % k == 0:
    print("Yes")
else:
    print("No")