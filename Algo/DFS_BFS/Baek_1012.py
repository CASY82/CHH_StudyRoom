#한번에 통과! 드디어 성장했구나!
import sys
sys.setrecursionlimit(10**5)
t = int(input())

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 0
    if graph[y][x] == 1:
        graph[y][x] = 0

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return 1

    return 0

for _ in range(t):
    m, n, k = map(int, input().split())

    result = []
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        x,y = map(int, input().split())

        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            result.append(dfs(j, i))

    print(sum(result))


#재귀 구문을 덜 써도 되는 코드 발견

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# for _ in range(int(input())):
#     ROW, COL, K = map(int, input().split())
#     MAPS = [[False for row in range(ROW)] for col in range(COL)]
#     for _ in range(K):
#         X, Y = map(int, input().split())
#         MAPS[Y][X] = True
#     answer = 0
#     def DFS(col, row):
#         x = [1, 0, -1, 0]
#         y = [0, 1, 0, -1]
#
#         for i in range(4):
#             if 0 <= col + y[i] < COL and 0 <= row + x[i] < ROW:
#                 if MAPS[col + y[i]][row + x[i]]:
#                     MAPS[col + y[i]][row + x[i]] = False
#                     DFS(col + y[i], row + x[i])                      # 내 코드는 4번의 재귀를 돌지만 해당 코드에서는 1번만 부른다
#     for col in range(COL):
#         for row in range(ROW):
#             if MAPS[col][row]:
#                 answer += 1
#                 MAPS[col][row] = False
#                 DFS(col, row)
#     print(answer)

#BFS 풀이

# from collections import deque
#
#
# def bfs(start_i, start_j):
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     visited[start_i][start_j] = True
#     q = deque([(start_i, start_j)])
#     while q:
#         i, j = q.popleft()
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < N and 0 <= nj < M:
#                 if field[ni][nj] == 1 and visited[ni][nj] == False:
#                     q.append((ni, nj))
#                     visited[ni][nj] = True
#
#
# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     field = [[0] * M for _ in range(N)]
#     visited = [[False] * M for _ in range(N)]
#     cnt = 0
#     for _ in range(K):
#         X, Y = map(int, input().split())
#         field[Y][X] = 1
#
#     for si in range(N):
#         for sj in range(M):
#             if field[si][sj] == 1 and visited[si][sj] == False:
#                 cnt += 1
#                 bfs(si, sj)
#     print(cnt)