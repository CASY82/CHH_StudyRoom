import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

num.sort()

#가운데 있는 수를 택하면 가장 차이가 작음
if len(num) % 2 == 0:
    center = len(num) // 2 - 1
else:
    center = len(num) // 2

print(num[center])