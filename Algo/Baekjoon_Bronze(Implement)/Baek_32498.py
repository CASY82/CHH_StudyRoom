import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    num = int(sys.stdin.readline())

    if num % 2 != 0:
        cnt += 1

print(cnt)