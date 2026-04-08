# 병영외 급식
import sys

n, x = map(int, sys.stdin.readline().split())
dormitory = list(map(int, sys.stdin.readline().split()))

if sum(dormitory) % x == 0:
    print(1)
else:
    print(0)