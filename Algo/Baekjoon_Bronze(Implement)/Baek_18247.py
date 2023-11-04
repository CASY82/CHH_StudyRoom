import sys

n = int(sys.stdin.readline())

# 11 , 4
for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())

    if n < 12:
        print(-1)
    else:
        if m < 4:
            print(-1)
        else:
            print(11 * m + 4)