# 소대 배정
import sys

a, b, n, k = map(int, sys.stdin.readline().split())

cnt = 1
res = [0, 0]

for i in range(a):
    for j in range(b):
        for z in range(n):
            if cnt == k:
                res[0] = i + 1
                res[1] = j + 1

            cnt += 1

print(*res)