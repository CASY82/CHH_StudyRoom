# 그래프와 그래프
import sys

a, b, c = map(int, sys.stdin.readline().split())

res = [[] for _ in range(10)]

for i in range(1, 11):
    for j in range(1, 11):
        if a * i + b * j == c:
            res[i - 1].append(j)

for data in res:
    if data:
        print(*data)
    else:
        print(0)