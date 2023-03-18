import sys
sys.setrecursionlimit(30000)

n = int(sys.stdin.readline())
colorpaper = []
cnt = [0, 0]

for _ in range(n):
    colorpaper.append(list(map(int, sys.stdin.readline().split())))

def quadTree(x, y, n):
    check = colorpaper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != colorpaper[i][j]:
                check = -1
                break

    if check == -1:
        n //= 2
        quadTree(x, y, n)
        quadTree(x, y + n, n)
        quadTree(x + n, y, n)
        quadTree(x + n, y + n, n)

    #0가 0, 1이 1
    elif check == 1:
        cnt[1] += 1
    else:
        cnt[0] += 1

quadTree(0, 0, n)
print(cnt[0])
print(cnt[1])