import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
city = []
visit = [[True for _ in range(n)] for _ in range(m)]
move = [[1, 0], [0, 1]]

for _ in range(m):
    city.append(list(map(int, sys.stdin.readline().split())))


queue = deque()
queue.append((0, 0))
visit[0][0] = False

while queue:
    nx, ny = queue.popleft()

    for i in range(len(move)):
        dx = nx + move[i][0]
        dy = ny + move[i][1]

        if 0 <= dx < n and 0 <= dy < m:
            if visit[dy][dx] and city[dy][dx] == 1:
                visit[dy][dx] = False
                queue.append((dx, dy))

if visit[m - 1][n - 1]:
    print("No")
else:
    print("Yes")

# 다른 사람 풀이
# from collections import deque as dq
# import sys
# input = sys.stdin.readline
#
# def bfs(x, y):
#     q = dq([(x, y)])
#     visited[x][y] = 1
#
#     while q:
#         x, y = q.popleft()
#
#         for dx, dy in move:
#             nx = x + dx
#             ny = y + dy
#
#             if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
#                 if city[nx][ny]:
#                     if nx == m - 1 and ny == n - 1:
#                         return 1
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#     return 0
#
# n, m = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(m)]
# visited = [[0] * n for _ in range(m)]
# move = [(0,1), (1, 0)]
#
# if (n == 1 and m == 1) or bfs(0, 0):
#     print("Yes")
# else:
#     print("No")