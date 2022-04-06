# 좀 더 연습이 필요... 외부에서 데이터를 조작하는 방법을 잘 모르는것 같다.
import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

nation = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for _ in range(n):
    nation.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y, visited, nation):
    global is_move
    population = nation[y][x]
    mov_cnt = 1
    que = deque()
    que.append((x, y))
    visited[y][x] = True
    temp = list()
    temp.append((x, y))

    while que:
        tx, ty = que.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx]:
                    if l <= abs(nation[ty][tx] - nation[ny][nx]) <= r:
                        visited[ny][nx] = True
                        que.append((nx, ny))
                        population += nation[ny][nx]
                        mov_cnt += 1
                        temp.append((nx, ny))

    # 인구 이동 완료 후 평균값으로 변경
    moving_complete = population // mov_cnt

    # 변경된 평균 값을 리스트에 다시 넣어줌
    if mov_cnt > 1:
        is_move = True
        for x, y in temp:
            nation[y][x] = moving_complete


while True:
    is_move = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(j, i, visited, nation)

    if is_move:
        cnt += 1
    else:
        break

print(cnt)