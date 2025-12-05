import sys

n = int(sys.stdin.readline())
woods = list(map(int, sys.stdin.readline().split()))

woods.sort()

if n < 4:
    print(0)
else:
    print(woods[-4] * woods[-4])