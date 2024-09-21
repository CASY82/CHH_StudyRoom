import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
res = 0

a.sort()
b.sort()

for i in range(3):
    res += a[i] * b[i]

print(res)