# import sys
# from collections import deque
#
# n, m = map(int, sys.stdin.readline().split())
# wall = []
# one_chance = [1]
#
# for _ in range(n):
#     wall.append(list(sys.stdin.readline().strip()))
#
# def bfs(x, y, cnt):
#     que = deque()
#     que.append((x, y, cnt))
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     while que:
#         tx, ty, distance = que.popleft()
#
#         if tx == m-1 and ty == n-1:
#             return distance
#
#         for i in range(4):
#             nx = tx + dx[i]
#             ny = ty + dy[i]
#
#             if 0 <= nx < m and 0 <= ny < n:
#                 if wall[ny][nx] == '0':
#                     que.append((nx, ny, distance+1))
#
#                 #벽 뚫기 구현 어케함?
#                 if wall[ny][nx] == '1' and one_chance[0] == 1:
#                     que.append((nx, ny, distance+1))
#                     one_chance[0] = 0
#
#         wall[ty][tx] = '2'
#
#     return -1
#
# result = bfs(0, 0, 1)
# print(result)
# print(wall)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
wall = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, crash):
    que = deque()
    que.append((x, y, crash))
    visited[y][x][crash] = 1

    while que:
        tx, ty, iscrash = que.popleft()

        if ty == n-1 and tx == m-1:
            return visited[ty][tx][iscrash]

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                #일반 이동(여기까진 기존에 구현 성공했으나 3차원으로 상태를 넣는것은 하지 못했다.)
                if wall[ny][nx] == 0 and visited[ny][nx][iscrash] == 0:
                    que.append((nx, ny, iscrash))
                    visited[ny][nx][iscrash] = visited[ty][tx][iscrash] + 1

                #벽 부수고 이동
                if wall[ny][nx] == 1 and iscrash == 0:
                    que.append((nx, ny, iscrash + 1))
                    # 즉 여기서 3차원 배열의 iscrash를 이용해서 벽을 부수고 이동했을때 상태 값이 갱신된다.
                    # +1 을 해줌으로 이전에 부수지 않았을때의 내용에서 전달 받는다.
                    visited[ny][nx][iscrash + 1] = visited[ty][tx][iscrash] + 1

    return -1

print(bfs(0, 0, 0))