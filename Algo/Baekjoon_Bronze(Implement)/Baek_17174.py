import sys

n, m = map(int, sys.stdin.readline().split())

cnt = n
tmp = n

while True:
    tmp //= m
    cnt += tmp

    if tmp < m:
        break

print(cnt)