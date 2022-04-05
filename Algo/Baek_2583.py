import sys
sys.setrecursionlimit(10 ** 8)

# 직사각형의 영역을 먼저 표시하면 된다. 그런 다음 dfs를 이용하면 끝
m, n, k = map(int, sys.stdin.readline().split())
cnt = 0
area = [[0 for _ in range(n)] for _ in range(m)]
result = []
tmp = [0]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if area[y][x] == 0:
        tmp[0] += 1
        area[y][x] = 2
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().split())

    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            area[i][j] = 1


for i in range(m):
    for j in range(n):
        tmp[0] = 0
        if dfs(j, i):
            cnt += 1
            result.append(tmp[0])


result.sort()
print(cnt)
print(*result)