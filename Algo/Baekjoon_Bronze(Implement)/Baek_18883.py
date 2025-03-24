import sys

n, m = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j < m:
            print(m * (i - 1) + j, end=" ")
        else:
            print(m * (i - 1) + j)