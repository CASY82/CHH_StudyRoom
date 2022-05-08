import sys
sys.setrecursionlimit(300000)

n, m = map(int, sys.stdin.readline().split())
cnt = 0
tile = []
for _ in range(n):
    tile.append(list(sys.stdin.readline().strip()))

def dfs(x, y, type):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if tile[y][x] == type:
        if type == "-":
            tile[y][x] = "0"
            dfs(x + 1, y, type)
            return True

        if type == "|":
            tile[y][x] = "0"
            dfs(x, y + 1, type)
            return True

    return False

for i in range(n):
    for j in range(m):
        if dfs(j, i, tile[i][j]):
            cnt += 1

print(cnt)