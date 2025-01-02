import sys

n, x = map(int, sys.stdin.readline().split())
max_late_start = 0

for _ in range(n):
    late_start, during_time = map(int, sys.stdin.readline().split())

    total_time = late_start + during_time
    if total_time <= x:
        max_late_start = max(max_late_start, late_start)

if max_late_start == 0:
    print(-1)
else:
    print(max_late_start)