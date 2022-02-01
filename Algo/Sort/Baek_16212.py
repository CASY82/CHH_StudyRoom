import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

for i in num:
    print(i, end=" ")