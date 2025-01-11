import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    score = []

    for i in range(m):
        score.append(list(map(int, sys.stdin.readline().split())))

    k, d, a = map(int, sys.stdin.readline().split())
    res = 0

    for i in range(m):
        res += max(k * score[i][0] - d * score[i][1] + a * score[i][2], 0)

    print(res)