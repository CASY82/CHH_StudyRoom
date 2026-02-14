# Small PhD Restaurant
import sys

n, m = map(int, sys.stdin.readline().split())
pay = list(map(int, sys.stdin.readline().split()))
give = list(map(int, sys.stdin.readline().split()))

tmp = []

for i in range(n):
    tmp.append([pay[i], give[i], give[i] - pay[i]])

tmp.sort(key=lambda x:(x[0], -x[2]))

for i in range(n):
    if tmp[i][0] <= m and tmp[i][2] > 0:
        m += tmp[i][2]

print(m)