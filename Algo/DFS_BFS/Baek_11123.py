import sys
sys.setrecursionlimit(300000)

t = int(sys.stdin.readline())

def dfs(x, y):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False

    if grid[y][x] == "#":
        grid[y][x] = "0"
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False

for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())

    grid = []
    cnt = 0

    for _ in range(h):
        grid.append(list(sys.stdin.readline().strip()))

    for i in range(h):
        for j in range(w):
            if dfs(j, i):
                cnt += 1

    print(cnt)