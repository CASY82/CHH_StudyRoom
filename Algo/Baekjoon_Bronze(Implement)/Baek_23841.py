# 데칼코마니
import sys

n, m = map(int, sys.stdin.readline().split())

picture = []

for _ in range(n):
    picture.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(m):
        if picture[i][j] != ".":
            if picture[i][m - (j + 1)] == ".":
                picture[i][m - (j + 1)] = picture[i][j]

for i in range(n):
    for j in range(m):
        print(picture[i][j], end="")
    print()