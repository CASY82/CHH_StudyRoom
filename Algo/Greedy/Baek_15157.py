import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

ans = [0] * n
min_base = 10 ** 18

for i in range(n):
    base = data[i] - (i + 1)
    if base < min_base:
        min_base = base

    day = i + 1
    ans[i] = day + min_base

print(*ans)