import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
tmp = 0
res = 0

for i in range(n - 1):
    if num[i] < num[i + 1]:
       tmp += num[i + 1] - num[i]
    else:
        res = max(tmp, res)
        tmp = 0

res = max(res, tmp)

print(res)