import sys

n, m = map(int, sys.stdin.readline().split())
stress = list(map(int, sys.stdin.readline().split()))

now = 0
res = 0

for val in stress:
    now += val

    if now < 0:
        now = 0

    if now >= m:
       res += 1

print(res)