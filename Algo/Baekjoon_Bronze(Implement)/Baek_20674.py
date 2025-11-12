import sys

n = int(sys.stdin.readline())
low = int(sys.stdin.readline())
res = 0

for _ in range(1, n):
    p = int(sys.stdin.readline())

    if low < p:
       res += p - low

    low = min(p, low)

print(res)