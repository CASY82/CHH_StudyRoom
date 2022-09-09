import sys
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split())
new_pixel = [[] for _ in range(n)]
result = 0

for sero in range(n):
    pixel = list(map(int, sys.stdin.readline().split()))

    tmp = []
    for pixnum in range(m * 3):
        tmp.append(pixel[pixnum])

        if pixnum % 3 == 2:
            new_pixel[sero].append(sum(tmp) // 3)
            tmp = []

t = int(sys.stdin.readline())

def dfs(x, y, t):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if new_pixel[y][x] >= t:
        new_pixel[y][x] = -1
        dfs(x + 1, y, t)
        dfs(x, y + 1, t)
        dfs(x - 1, y, t)
        dfs(x, y - 1, t)

        return True

    return False

for i in range(n):
    for j in range(m):
        if dfs(j, i, t):
            result += 1

print(result)