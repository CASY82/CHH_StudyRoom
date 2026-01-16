# Exact Change

import sys

n = int(sys.stdin.readline())
money = [150, 30, 15, 5, 1]
cnt = [0, 0, 0, 0, 0]

for i in range(5):
    cnt[i] = n // money[i]
    n %= money[i]

cnt.reverse()

print(*cnt)