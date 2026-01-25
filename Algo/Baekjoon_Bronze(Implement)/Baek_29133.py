# Фома и занимательная математика
import sys

a, b, c, d = map(int, sys.stdin.readline().split())
cnt = 0
res = 0

for i in range(1, 4):
    if a ** i + b ** i + c ** i == d:
        cnt += 1
        res = i

if cnt == 1:
    print(res)
else:
    print(-1)