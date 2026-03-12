# 다오의 경주 대회
import sys

n, k = map(int, sys.stdin.readline().split())
tracks = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(1, n):
    if tracks[i - 1] >= tracks[i] + k:
        cnt = -1
        break
    else:
        if tracks[i - 1] >= tracks[i]:
            cnt += 1
            tracks[i] += k

print(cnt)