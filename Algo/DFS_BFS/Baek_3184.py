import sys
sys.setrecursionlimit(10 ** 5)

r, c = map(int, sys.stdin.readline().split())

land = []
sheep = 0
wolf = 0

for _ in range(r):
    land.append(list(sys.stdin.readline().strip()))

def dfs(x, y):
    if x < 0 or y < 0 or x >= c or y >= r:
        return

    if land[y][x] != '#':
        if land[y][x] == 'v':
            tmp[0] += 1
        elif land[y][x] == 'o':
            tmp[1] += 1

        land[y][x] = '#'
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return

    return

for i in range(r):
    for j in range(c):
        tmp = [0, 0]
        dfs(j, i)

        if tmp[0] < tmp[1]:
            tmp[0] = 0
        else:
            tmp[1] = 0

        wolf += tmp[0]
        sheep += tmp[1]

print(sheep, wolf)