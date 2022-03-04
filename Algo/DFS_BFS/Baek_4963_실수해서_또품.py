import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x, y, w, h, land):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False

    if land[y][x] == 1:
        land[y][x] = 0
        dfs(x + 1, y, w, h, land)
        dfs(x - 1, y, w, h, land)
        dfs(x, y + 1, w, h, land)
        dfs(x, y - 1, w, h, land)
        dfs(x - 1, y - 1, w, h, land)
        dfs(x + 1, y - 1, w, h, land)
        dfs(x - 1, y + 1, w, h, land)
        dfs(x + 1, y + 1, w, h, land)
        return True

    return False

while True:
    w, h = map(int, sys.stdin.readline().split())
    land = []
    cnt = 0

    if w == 0 and h == 0:
        break

    for _ in range(h):
        land.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if dfs(j, i, w, h, land):
                cnt += 1

    print(cnt)