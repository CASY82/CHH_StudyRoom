import sys

n = int(sys.stdin.readline())

origin = list(map(int, sys.stdin.readline().split()))
last = list(map(int, sys.stdin.readline().split()))

res = 0

for i in range(n):
    if origin[i] > last[i]:
        res += (origin[i] - last[i])

print(res)