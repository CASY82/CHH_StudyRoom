import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

tmp = []

if n < m:
    for i in range(n):
        if a[i] in b and a[i] not in tmp:
            tmp.append(a[i])
else:
    for i in range(m):
        if b[i] in a and b[i] not in tmp:
            tmp.append(b[i])

tmp.sort()

for res in tmp:
    print(res)