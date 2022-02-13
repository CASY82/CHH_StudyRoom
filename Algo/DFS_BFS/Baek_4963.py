import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, w, h, arr):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False

    if arr[y][x] == 1:
        arr[y][x] = 0
        dfs(x + 1, y, w, h, arr)
        dfs(x - 1, y, w, h, arr)
        dfs(x, y + 1, w, h, arr)
        dfs(x, y - 1, w, h, arr)
        dfs(x + 1, y + 1, w, h, arr)
        dfs(x + 1, y - 1, w, h, arr)
        dfs(x - 1, y + 1, w, h, arr)
        dfs(x - 1, y - 1, w, h, arr)

        return True

    return False
while True:
    w, h = map(int, sys.stdin.readline().split())
    cnt = 0
    land_map = []

    if w == 0 and h == 0:
        break

    for _ in range(h):
        land_map.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if dfs(j, i, w, h, land_map):
                cnt += 1

    print(cnt)
