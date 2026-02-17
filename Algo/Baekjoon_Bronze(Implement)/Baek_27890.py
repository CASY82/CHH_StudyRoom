# 특별한 작은 분수
import sys

x, n = map(int, sys.stdin.readline().split())

# 수식
for t in range(1, n + 1):
    if x % 2 == 0:
        x = (x // 2) ^ 6
    else:
        x = (x * 2) ^ 6

print(x)