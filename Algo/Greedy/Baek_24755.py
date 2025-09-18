import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort(reverse=True)

res = 0

for i in range(n):
    if n // 2 > i:
        res += p[i]
    else:
        res += p[i] // 2

print(res)