import sys
sys.setrecursionlimit(300000)
n, m = map(int, sys.stdin.readline().split())

board = []
visited = [[True for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
    tmp = list(sys.stdin.readline().strip())
    board.append(tmp)

def dfs(x, y, cyclenum, color, cnt):
    if board[y][x] == color:
        visited[y][x] = False

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if (nx, ny) == cyclenum and cnt >= 4:
                print("Yes")
                exit()
            if visited[ny][nx]:
                dfs(nx, ny, cyclenum, color, cnt + 1)
                visited[ny][nx] = True #이건 몰랐네;;

        return True

for i in range(n):
    for j in range(m):
        cyclenum = (j, i)
        dfs(j, i, cyclenum, board[i][j], 1)

print("No")

# 16929번 Two Dots

# from sys import stdin
# input = stdin.readline
#
# # 사이클이 존재하는지 확인하는 함수
# def cycle(color, x, y, cnt, start_x, start_y):
#     global ans
#     # 이미 사이클을 찾았다면 종료
#     if ans is True:
#         return
#     # 4가지 방향에 대하여
#     for i in range(4):
#         # 이동 위치 좌표 설정
#         nx, ny = x + dx[i], y + dy[i]
#         # 이동 위치가 게임판을 벗어나면 건너뛰기
#         if nx < 0 or nx >= n or ny < 0 or ny >= m:
#             continue
#         # 사이클이 존재(4개 이상 점 연결, 처음 시작지점 도달)한다면
#         if cnt >= 4 and nx == start_x and ny == start_y:
#             # 정답 존재 표시
#             ans = True
#             return
#         # 색깔이 같고 아직 방문하지 않았다면
#         if board[nx][ny] == color and visited[nx][ny] == 0:
#             # 방문 표시
#             visited[nx][ny] = 1
#             # 재귀적으로 수행
#             cycle(color, nx, ny, cnt + 1, start_x, start_y)
#             # 방문 표시 해제
#             visited[nx][ny] = 0
#
# # 게임 시작 함수
# def game_start():
#     for i in range(n):
#         for j in range(m):
#             # 사이클 시작 위치 좌표
#             start_x, start_y = i, j
#             # 방문 표시
#             visited[start_x][start_y] = 1
#             # 사이클이 존재하는지 함수 실시
#             cycle(board[i][j], i, j, 1, start_x, start_y)
#             # 사이클이 존재한다면
#             if ans:
#                 return 'Yes'
#     # 사이클이 존재하지 않는다면
#     return 'No'
#
# n, m = map(int, input().split())
# board = [[a for a in input().rstrip()] for _ in range(n)]
# # 방문
# visited = [[0] * m for _ in range(n)]
# # 동, 남, 서, 북 방향 표시
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# # 정답 변수
# ans = False
#
# # 정답 출력
# print(game_start())