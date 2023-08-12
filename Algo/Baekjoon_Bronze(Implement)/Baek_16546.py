import sys

n = int(sys.stdin.readline())
runner = set(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):
    if i not in runner:
        print(i)
        break