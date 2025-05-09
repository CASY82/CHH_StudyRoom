import sys

n = int(sys.stdin.readline())
trash = list(map(int, sys.stdin.readline().split()))

print(trash.index(min(trash)))