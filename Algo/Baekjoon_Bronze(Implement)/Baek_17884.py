# Lost Lineup

import sys

n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))

tmp = []

for i in range(n - 1):
    tmp.append((d[i], i + 2))

tmp.sort(key=lambda x:x[0])

res = [1]

for k, v in tmp:
    res.append(v)

print(*res)