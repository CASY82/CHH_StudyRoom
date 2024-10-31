import sys

n, a, b, c = map(int, sys.stdin.readline().split())

total = 0

if n != 1:
    if min(a, b, c) == a:
        total += a * (n - 1)
    elif min(a, b, c) == b:
        total += b * (n - 1)
    else:
        total += min(a, b) + c * (n - 2)

print(total // 100, total % 100)