import sys

n = int(sys.stdin.readline())

village = list(map(int, sys.stdin.readline().split()))

print(sum(village)-max(village))