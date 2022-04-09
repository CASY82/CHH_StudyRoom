import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

data_sum = [-1001 for _ in range(n + 1)]

data_sum[0] = data[0]

for i in range(1, n):
     data_sum[i] = max(data_sum[i-1] + data[i], data[i])

print(max(data_sum))