# import sys
# sys.setrecursionlimit(500000)
#
# n, m = map(int, sys.stdin.readline().split())
# d = [0]
#
# # d 0: 북, 1: 동, 2: 남, 3: 서
# start_x, start_y, d[0] = map(int, sys.stdin.readline().split())
#
# room = []
# visited = [[True for _ in range(m)] for _ in range(n)]
#
# result = [0]
#
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# for row in range(n):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     room.append(tmp)
#
#     for col in range(m):
#         if tmp[col] == 1:
#             visited[row][col] = False
#
# # 현재 칸이 청소 되었는가
# # 현재 칸 주변 4칸 전부 청소된 경우
# # 1) 방향 유지한채로 한칸 후진 가능하면 후진
# # 2) 뒤가 벽이라 후진 못하면 ㅈㅈ
# # 주변 4칸중 청소되지 않은 칸이 있으면
# # 1) 반시계 90도 회전
# # 2) 바라보는 방향 기준으로 앞쪽칸이 청소 안된 구역이면 전진
# # 3) 청소
# # ---
# # 0 : 청소 안됨 / 1 : 벽 / 2 : 임의로 청소된 곳이라 칭하자
#
# def dfs(x, y):
#     if x < 0 or x >= m or y < 0 or y >= n:
#         return
#
#     visited[y][x] = False
#     result[0] += 1
#
#     # 뒤로 후진해야 할까? 체크
#     turn = True
#
#     for dir in range(4):
#         # 주변 4칸 청소가 안되어 있는가
#         if visited[dx[dir]][dy[dir]]:
#             d[0] = dir
#             # 뒤로 후진할 필요 없음
#             turn = False
#             dfs(x + dx[dir], y + dy[dir])
#
#     # 뒤로 후진
#     if turn:
#         d[0] = (d[0] + 2) % 4
#         if room[y + dy[d[0]]][x + dx[d[0]]] != 1:
#             dfs(x + dx[d[0]], y + dy[d[0]])
#         else:
#             return
#
# dfs(start_x, start_y)
#
# print(result[0])

import sys

n, m = map(int, sys.stdin.readline().split())

room = []
visited = [[True] * m for _ in range(n)]

r, c, d = map(int,input().split())

# 반시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

# 시작 지점
visited[r][c] = False
cnt = 1

while True:
    # 4방향 청소 여부 확인
    flag = 0

    for _ in range(4):
        # 반시계를 맞춰주기 위함
        nx = r + dx[(d+3) % 4]
        ny = c + dy[(d+3) % 4]

        d = (d+3) % 4

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            if visited[nx][ny]:
                visited[nx][ny] = False
                cnt += 1
                r = nx
                c = ny

                # 청소를 한 방향이라도 했다면 다음 시퀀스로
                flag = 1
                break

    if flag == 0: # 4방향 모두 청소
        if room[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]