import sys

n, m, k = map(int, sys.stdin.readline().split())
result = 0

x_cnt = n-m

# O를 K개 그리고 N-K개가 X
if m >= k:
    result += k + x_cnt
else:
    result += m + (n - k)

print(result)