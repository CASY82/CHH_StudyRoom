import sys

# 최장 증가 부분 수열(LIS) 이용
n = int(sys.stdin.readline())
child = []
dp = [1] * n

for _ in range(n):
    child.append(int(sys.stdin.readline()))

for i in range(1, n):
    for j in range(i):
        if child[j] < child[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)

print(n - max_len)