# Tabbtabbande
import sys

n, m = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

now = 1
res = 0

for i in range(m):
    res += min(abs(seq[i] - now), n - abs(now - seq[i]))
    now = seq[i]

print(res)