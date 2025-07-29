import sys

data = list(map(int, sys.stdin.readline().split()))

data.sort()

print(data[1] + data[2] + data[3] + 1)