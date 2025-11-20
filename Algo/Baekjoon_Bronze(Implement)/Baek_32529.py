import sys

n, m = map(int, sys.stdin.readline().split())
lose = list(map(int, sys.stdin.readline().split()))

res = -1
s = 0

if m > sum(lose):
    print(-1)
else:
    for i in range(n - 1, -1, -1):
        s += lose[i]

        if m <= s:
            res = i + 1
            break

    print(res)