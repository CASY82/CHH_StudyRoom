import sys

n, t = map(int, sys.stdin.readline().split())

work = list(map(int, sys.stdin.readline().split()))

cnt = 0
work_sum = 0

for i in work:
    if work_sum + i <= t:
        work_sum += i
        cnt += 1
    else:
        break

print(cnt)