import sys

c = int(sys.stdin.readline())

for _ in range(c):
    n = int(sys.stdin.readline())

    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    print(n, cnt)