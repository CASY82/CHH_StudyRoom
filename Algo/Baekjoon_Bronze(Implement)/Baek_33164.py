import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(len(a)):
    for j in range(len(b)):
        res += (a[i] + b[j]) * max(a[i], b[j])

print(res)