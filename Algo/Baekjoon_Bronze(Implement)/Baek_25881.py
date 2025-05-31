import sys

a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

for _ in range(n):
    used_electric = int(sys.stdin.readline())
    res = 0

    if used_electric <= 1000:
        res += used_electric * a
    else:
        res += 1000 * a + (used_electric - 1000) * b

    print(used_electric, res)