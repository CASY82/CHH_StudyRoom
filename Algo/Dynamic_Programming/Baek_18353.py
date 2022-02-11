#LIS DP문제~
import sys

n = int(sys.stdin.readline())
soldier = list(map(int, sys.stdin.readline().split()))

remain = [0 for _ in range(n)]

for i in range(n):
    remain[i] = 1
    for j in range(i):
        if soldier[i] < soldier[j]:
            remain[i] = max(remain[i], remain[j] + 1)

print(n - max(remain))