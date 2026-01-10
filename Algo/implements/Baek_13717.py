# 포켓몬 GO

import sys

n = int(sys.stdin.readline())
total = 0
tmp = []

for i in range(n):
    name = sys.stdin.readline().strip()
    k, m = map(int, sys.stdin.readline().split())
    cnt = 0

    while m >= k:
        m -= k
        m += 2
        cnt += 1

    tmp.append([cnt, i, name])
    total += cnt

tmp.sort(key=lambda x:(x[0], -x[1]))

print(total)
print(tmp[-1][-1])