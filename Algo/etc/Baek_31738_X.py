import sys

n, m = map(int, sys.stdin.readline().split())
res = 1

if n < m:
    for i in range(1, n + 1):
        res *= i
        res %= m

    print(res % m)
else:
    print(0)