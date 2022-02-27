import sys

n = int(sys.stdin.readline())
Acnt = 0
Bcnt = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        Acnt += 1
    elif a < b:
        Bcnt += 1
    else:
        continue

print(Acnt, Bcnt)