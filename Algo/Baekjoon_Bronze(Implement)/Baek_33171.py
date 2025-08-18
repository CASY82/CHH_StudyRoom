import sys

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
cnt = 0

for i in range(1, n + 1):
    if (i % a == 0 and i % b != 0) or (i % a != 0 and i % b == 0):
        cnt += 1

print(cnt)