import sys

a, b = map(int, sys.stdin.readline().split())
res = 0

if a % 2 == 0 or b % 2 == 1:
    res += 1

res += (b - a + 1) // 2

print(res)