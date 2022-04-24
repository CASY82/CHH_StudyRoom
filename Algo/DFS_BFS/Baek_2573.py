# pypy로 통과!
import sys
sys.setrecursionlimit(300000)

n, m = map(int, sys.stdin.readline().split())

glacier = []
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    glacier.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if glacier[y][x] == 0:
        return False

    if glacier[y][x] > 0 and visited[y][x] == 0:
        visited[y][x] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
                if glacier[y][x] > 0:
                    glacier[y][x] -= 1
                else:
                    break

        return True

    return False

while True:
    land = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if dfs(j, i):
                land += 1

    if land >= 2:
        break

    if land == 0:
        result = 0
        break

    result += 1

print(result)

# python으로 통과한 코드
# import sys
# from collections import deque
#
#
# input = sys.stdin.readline
#
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
#
# def bfs(deq, visited):
#     meltList = []
#     while deq:
#         curY, curX = deq.popleft()
#         for i in range(4):
#             ny, nx = curY+dy[i], curX+dx[i]
#             if 0 <= ny < n and 0 <= nx < m:
#                 if board[ny][nx] == 0:
#                     meltList.append([curY, curX])
#                     continue
#                 if not visited[ny][nx]:
#                     deq.append([ny, nx])
#                     visited[ny][nx] = True
#     for y, x in meltList:
#         board[y][x] = board[y][x]-1 if board[y][x] > 0 else 0
#
#
# def main():
#     cnt = 0
#     while True:
#         endCnt = 0
#         visited = [[False]*m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] != 0 and not visited[i][j]:
#                     if endCnt > 0:
#                         return cnt
#                     visited[i][j] = True
#                     bfs(deque([[i, j]]), visited)
#                     endCnt += 1
#         if endCnt == 0:
#             return 0
#         cnt += 1
#
#
# print(main())