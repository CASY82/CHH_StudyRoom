import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())

jump = []
check = [False]

for _ in range(n):
    jump.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return

    if x == n - 1 and y == n - 1:
        check[0] = True
        return

    if jump[y][x] == 0:
        return

    dfs(x + jump[y][x], y)
    dfs(x, y + jump[y][x])

dfs(0, 0)

if check[0]:
    print("HaruHaru")
else:
    print("Hing")