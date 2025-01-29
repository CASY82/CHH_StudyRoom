import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = set(map(int, sys.stdin.readline().split()))

res = 0

for i in range(n):
    res += a[i]

    if res in b:
        res = 0

print(res)