import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0

    for b in range(1, n):
        for a in range(1, b):
           if (a*a + b*b + m) % (a*b) == 0:
               cnt += 1

    print(cnt)