import sys

r, c = map(int, sys.stdin.readline().split())

island = []
new_island = [[] for _ in range(r)]

for _ in range(r):
    island.append(list(sys.stdin.readline().strip()))

for i in range(r):
    for j in range(c):
        cnt = 0
        if island[i][j] == "X":
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + y < r and 0 <= j + x < c:
                    if island[i + y][j + x] == ".":
                        cnt += 1
                else:
                    cnt += 1

        if cnt >= 3:
            new_island[i].append(".")
        else:
            new_island[i].append(island[i][j])

r_min, r_max = r, -1
c_min, c_max = c, -1

for i in range(r):
    for j in range(c):
        if new_island[i][j] == 'X':
            r_min = min(r_min, i)
            r_max = max(r_max, i)
            c_min = min(c_min, j)
            c_max = max(c_max, j)

for i in range(r_min, r_max + 1):
    print(''.join(new_island[i][c_min:c_max + 1]))