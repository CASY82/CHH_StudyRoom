import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())
    cnt = 0
    i = 5
    while num // i >= 1:
        cnt += num // i
        i *= 5

    print(cnt)