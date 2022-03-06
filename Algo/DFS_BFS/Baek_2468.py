import copy
import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
land = []

for _ in range(n):
    land.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y, n, target, array):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if land[y][x] >= target and array[y][x] != 101:
        array[y][x] = 101
        dfs(x - 1, y, n, target, array)
        dfs(x + 1, y, n, target, array)
        dfs(x, y - 1, n, target, array)
        dfs(x, y + 1, n, target, array)
        return True

    return False


max_land_cnt = 0

for height in range(1, 101):
    cnt = 0
    tmp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(j, i, n, height, tmp):
                cnt += 1

    if max_land_cnt < cnt:
        max_land_cnt = cnt

print(max_land_cnt)