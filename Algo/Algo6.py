h, w = map(int, input().split())
n = int(input())

panel = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())

    x = x-1
    y = y-1

    for j in range(l):
        if d == 0:
            panel[x][y+j] = 1
        else:
            panel[x+j][y] = 1


for i in range(h):
    for j in range(w):
        print(panel[i][j], end=' ')

    print()


