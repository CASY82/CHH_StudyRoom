import sys

n = int(sys.stdin.readline())
stric = list(map(int, sys.stdin.readline().split()))
cnt = 0
max_cnt = 0

for i in range(n):
    if stric[i] == 0:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
    else:
        cnt += 1

max_cnt = max(max_cnt, cnt)
print(max_cnt)