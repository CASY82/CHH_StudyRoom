import sys

n, m = map(int, sys.stdin.readline().split())
cube = []
res = 0

for _ in range(n):
    cube.append(list(map(int, sys.stdin.readline().split())))

# 동-서 방향 옆면
east_west = 0
for i in range(n):
    east_west += cube[i][0]          # 왼쪽 바깥
    east_west += cube[i][m-1]        # 오른쪽 바깥
    for j in range(1, m):
        east_west += abs(cube[i][j] - cube[i][j-1])

# 남-북 방향 옆면
north_south = 0
for j in range(m):
    north_south += cube[0][j]        # 위 바깥
    north_south += cube[n-1][j]      # 아래 바깥
    for i in range(1, n):
        north_south += abs(cube[i][j] - cube[i-1][j])

# 위/아래 계산
top_bottom = 0
for i in range(n):
    for j in range(m):
        if cube[i][j] > 0:
            top_bottom += 2

res += north_south + east_west + top_bottom

print(res)