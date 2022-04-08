import sys
from collections import deque

n = int(sys.stdin.readline())
sea = []

for _ in range(n):
    sea.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
shark_size = 2
shark_x, shark_y = 0, 0

# 아기 상어의 최초 좌표를 입력한다.
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark_x = j
            shark_y = i

# bfs는 최소 경로라는 것을 보장하므로 bfs를 이용
def bfs(x, y, shark_size):
    # 전체 거리를 일단 받는다.
    distance = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    que = deque()
    que.append((x, y))
    visited[y][x] = 1
    # 먹을 수 있는 물고기를 담는 리스트
    temp = []

    while que:
        cur_x, cur_y = que.popleft()

        # 이부분은 우리가 아는 bfs 그대로~
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                if sea[ny][nx] <= shark_size:
                    que.append((nx, ny))
                    visited[ny][nx] = 1
                    # distance를 따로 만든 이유가 여기 나온다. 전체의 맵에 거리를 표시
                    distance[ny][nx] = distance[cur_y][cur_x] + 1
                    # 상어가 잡아먹은 물고기를 담아준다.
                    if sea[ny][nx] < shark_size and sea[ny][nx] != 0:
                        temp.append((nx, ny, distance[ny][nx]))

    # 정렬해서 리턴
    return sorted(temp, key=lambda x : (-x[2], -x[1], -x[0]))

result = 0

while True:
    shark = bfs(shark_x, shark_y, shark_size)

    # 만약 잡아먹을 수 있는게 없다면 중지
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    # 정렬된 잡아먹은 물고기 배열에서 마지막 녀석을 가져온다.
    # 역순으로 정렬한 이유가 여기서 나온다.
    result += dist

    # 해당 위치를 전부 0으로 변경해준다(물고기를 먹었으므로)
    sea[shark_y][shark_x], sea[ny][nx] = 0, 0

    # 상어도 위치가 변경 되어야한다.
    shark_x, shark_y = nx, ny

    # 물고기를 먹었으므로 카운트 증가
    cnt += 1
    # 자기 몸집 만큼 먹었다면 몸집 증가!
    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(result)