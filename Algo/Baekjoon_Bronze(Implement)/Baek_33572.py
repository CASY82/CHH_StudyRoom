import sys

n, m = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

tmp = sum(times)
tmp -= n

if tmp >= m:
    print("DIMI")
else:
    print("OUT")