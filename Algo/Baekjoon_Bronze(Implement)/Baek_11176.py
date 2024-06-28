import sys

t = int(sys.stdin.readline())

for _ in range(t):
    e, n = map(int, sys.stdin.readline().split())
    cnt = 0

    for i in range(n):
        shampoo = int(sys.stdin.readline())

        if shampoo > e:
            cnt += 1

    print(cnt)