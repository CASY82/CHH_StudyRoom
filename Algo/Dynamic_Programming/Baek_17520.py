import sys

n = int(sys.stdin.readline())
MOD = 16769023
res = 1

for i in range(1, n + 1):
    if i % 2 == 1:
        res *= 2

    res %= MOD

print(res)