# Dangerous Dive

import sys

n, r = map(int, sys.stdin.readline().split())
volunteer = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(1, n + 1):
    if i not in volunteer:
        res.append(i)

if res:
    print(*res)
else:
    print("*")