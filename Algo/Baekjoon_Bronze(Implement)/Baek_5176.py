import sys

k = int(sys.stdin.readline())

for _ in range(k):
    p, m = map(int, sys.stdin.readline().split())

    sit = [True] * m
    sunjum = []
    cnt = 0

    for _ in range(p):
        sunjum.append(int(sys.stdin.readline()))

    for i in range(len(sunjum)):
        if sit[sunjum[i]-1]:
            sit[sunjum[i]-1] = False
            cnt += 1

    print(len(sunjum) - cnt)