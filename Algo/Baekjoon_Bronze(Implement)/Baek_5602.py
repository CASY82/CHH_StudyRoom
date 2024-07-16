import sys

n, m = map(int, sys.stdin.readline().split())

place = [0 for _ in range(m)]
tmp = []

for _ in range(n):
    score = list(map(int, sys.stdin.readline().split()))

    for i in range(m):
        place[i] += score[i]

for i in range(m):
    tmp.append((place[i], i + 1))

tmp.sort(key=lambda x:(-x[0], x[1]))

for i in range(m):
    print(tmp[i][1], end=" ")


# 다른 사람 풀이
# import sys
# n, m = map(int, sys.stdin.readline().split())
# ls = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# d = {i: [] for i in range(n + 1)}
# for i in range(m):
#     c = sum([j[i] for j in ls])
#     d[c].append(str(i + 1))
# o = []
# for i in range(n + 1):
#     if len(d[n - i]) > 0:
#         o.append(' '.join(d[n - i]))
# print(' '.join(o))