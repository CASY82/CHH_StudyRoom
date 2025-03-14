import sys

w, n, p = map(int, sys.stdin.readline().split())
punches = list(map(int, sys.stdin.readline().split()))
res = 0

for check in punches:
    if w <= check <= n:
        res += 1

print(res)