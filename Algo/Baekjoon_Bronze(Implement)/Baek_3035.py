import sys

r, c, zr, zc = map(int, sys.stdin.readline().split())

origin = []

for _ in range(r):
    origin.append(list(sys.stdin.readline().strip()))

result = []
tmp = []

for row in range(r):
    for col in range(c):
        for z_col in range(zc):
            tmp.append(origin[row][col])

    for z_row in range(zr):
        result.append(tmp)

    tmp = []

for i in range(zr * r):
    for j in range(zc * c):
        print(result[i][j], end="")
    print()