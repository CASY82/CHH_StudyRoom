# Internetas
import sys

n = int(sys.stdin.readline())
long_time = 0
now_time = 0

for _ in range(n):
    t, m = map(int, sys.stdin.readline().split())

    if m == 1:
        long_time = max(t - now_time, long_time)
        now_time = t

print(long_time)