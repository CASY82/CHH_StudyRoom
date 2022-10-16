import sys

n, d = map(int, sys.stdin.readline().split())

num_cnt = [0 for _ in range(10)]

for i in range(1, n+1):
    tmp = str(i)
    for j in range(len(tmp)):
        num_cnt[int(tmp[j])] += 1

print(num_cnt[d])