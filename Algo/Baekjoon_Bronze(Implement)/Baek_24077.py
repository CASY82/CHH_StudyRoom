# 比較 (Comparison)
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(n):
    for j in range(m):
        if a[i] <= b[j]:
            cnt += 1

print(cnt)