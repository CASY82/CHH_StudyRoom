import sys

n, k = map(int, sys.stdin.readline().split())
data = []

for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

res = 0
start = 0

for end in range(n):
    while data[end] - data[start] > k:
        start += 1

    res = max(res, end - start + 1)

print(res)