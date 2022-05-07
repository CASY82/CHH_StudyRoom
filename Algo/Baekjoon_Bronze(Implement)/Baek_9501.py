import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())

    space_shuttle = []
    cnt = 0

    for i in range(n):
        v, f, c = map(int, sys.stdin.readline().split())

        result = v * (f / c)

        if result >= d:
            cnt += 1

    print(cnt)