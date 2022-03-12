import sys

n = int(sys.stdin.readline())
cnt = 0

for a in range(1, 501):
    for b in range(1, a+1):
        if (a * a) == (b * b + n):
            cnt += 1

print(cnt)