import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0 for _ in range(n)]
all_sum = sum(num)
result = 0

#당연히 시간초과.. 쉐키
# for i in range(n):
#     for j in range(i+1, n):
#         result += num[i] * num[j]

prefix_sum[0] = num[0]
for i in range(1, n):
    prefix_sum[i] = num[i] + prefix_sum[i-1]

for i in range(n):
    result += num[i] * (all_sum - prefix_sum[i])

print(result)