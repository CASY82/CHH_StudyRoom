import sys
import copy
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
color = []
cnt = [0]
redcnt = [0]

for _ in range(n):
    color.append(list(sys.stdin.readline().strip()))

color_red = copy.deepcopy(color)

def dfs(x, y, same_color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if same_color == 'R' or same_color == 'G' or same_color == 'B':
        if same_color == color[y][x]:
            color[y][x] = cnt[0]
            dfs(x + 1, y, same_color)
            dfs(x - 1, y, same_color)
            dfs(x, y + 1, same_color)
            dfs(x, y - 1, same_color)

            return True

    return False

def reddfs(x, y, same_color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if color_red[y][x] == 'R' or color_red[y][x] == 'G':
        if same_color != 'B':
            color_red[y][x] = redcnt[0]
            reddfs(x + 1, y, same_color)
            reddfs(x - 1, y, same_color)
            reddfs(x, y + 1, same_color)
            reddfs(x, y - 1, same_color)

            return True
    elif color_red[y][x] == 'B':
        if same_color == color_red[y][x]:
            color_red[y][x] = redcnt[0]
            reddfs(x + 1, y, same_color)
            reddfs(x - 1, y, same_color)
            reddfs(x, y + 1, same_color)
            reddfs(x, y - 1, same_color)

            return True

    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j, color[j][i]):
            cnt[0] += 1

        if reddfs(i, j, color_red[j][i]):
            redcnt[0] += 1

print(cnt[0], redcnt[0])