import sys

n, k = map(int, sys.stdin.readline().split())

res = []

for i in range(1, k+1):
    tmp = str(n*i)
    tmp = int(tmp[::-1])

    res.append(tmp)

print(max(res))