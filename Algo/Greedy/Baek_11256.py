import sys

t = int(sys.stdin.readline())

for _ in range(t):
    j, n = map(int, sys.stdin.readline().split())
    box = []

    for _ in range(n):
        c, r = map(int, sys.stdin.readline().split())
        box.append(c * r)

    box.sort(reverse=True)
    cnt = 0

    for i in box:
        j -= i
        cnt += 1
        if j <= 0:
            break

    print(cnt)