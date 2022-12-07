import sys

num = list(map(int, sys.stdin.readline().split()))

num.sort()

if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
    print(1)
elif num[0] == num[1] == num[2]:
    print(2)
else:
    print(0)