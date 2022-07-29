import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
interval_sum = []

interval_sum.append(num[0])

for no in range(1, n):
    interval_sum.append(interval_sum[-1] + num[no])

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    if i == 1:
        print(interval_sum[j-1])
    else:
        print(interval_sum[j-1] - interval_sum[i-2])