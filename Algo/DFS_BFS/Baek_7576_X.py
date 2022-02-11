# 흠... 뭘로 풀어야 하는지는 알지만 bfs숙련도가 낮아서 참고하여 그냥 품
import sys
from collections import deque

# 1은 익은 트메이러
# 0은 익지 않은 트메이러
# -1은 없는 칸

m, n = map(int, sys.stdin.readline().split())
box = []
tomato = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0

for i in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

    for j in range(m):
        if box[i][j] == 1:
            tomato.append([i, j])

# bfs를 이용
def boxSearch():
    while tomato:
        x, y = tomato.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                #횟수를 따로 구하지 않고 숫자를 그냥 더해서 변경하는 형태
                box[nx][ny] = box[x][y] + 1
                tomato.append([nx, ny])

boxSearch()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    #따로 구하지 않았으므로 max값이 곧 날짜
    result = max(result, max(i))
#첫날 빼주기
print(result - 1)