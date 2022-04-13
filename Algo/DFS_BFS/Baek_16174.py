import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())

land = []
check = [False]

for _ in range(n):
    land.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return

    if x == n - 1 and y == n - 1:
        check[0] = True
        return

    if land[y][x] == 0:
        return

    if visited[y][x]:
        return

    visited[y][x] = True
    dfs(x + land[y][x], y)
    dfs(x, y + land[y][x])

dfs(0, 0)
if check[0]:
    print("HaruHaru")
else:
    print("Hing")