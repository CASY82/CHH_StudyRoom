import sys

n = int(sys.stdin.readline())
res = 9999999999999999

for _ in range(n):
    need, have = map(int, sys.stdin.readline().split())

    res = min(res, have // need)

print(res)