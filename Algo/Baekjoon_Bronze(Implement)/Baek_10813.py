import sys

n, m = map(int, sys.stdin.readline().split())
num = [(i+1) for i in range(n)]

for j in range(m):
    first, second = map(int, sys.stdin.readline().split())

    num[first-1], num[second-1] = num[second-1], num[first-1]

print(*num)