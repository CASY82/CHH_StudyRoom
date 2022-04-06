# 내 코드는 pypy로 통과하였다.
import sys
from collections import deque

l, w = map(int, sys.stdin.readline().split())
treasure_map = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(l):
    treasure_map.append(list(sys.stdin.readline().strip()))

def bfs(x, y):
    que = deque()
    visited = [[0 for _ in range(w)] for _ in range(l)]
    que.append((x, y, 1))
    visited[y][x] = 1

    while que:
        tx, ty, cnt = que.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < w and 0 <= ny < l:
                if treasure_map[ny][nx] == "L" and visited[ny][nx] == 0:
                    visited[ny][nx] = cnt
                    que.append((nx, ny, cnt + 1))

    return cnt

max_distance = 0
for i in range(l):
    for j in range(w):
        if treasure_map[i][j] == 'L':
            distance = bfs(j, i)
            if max_distance < distance:
                max_distance = distance

print(max_distance-1)


# 아래코드는 파이썬으로 통과한 코드.. 똑같은거 같은데 저건 왜 통과일까?(다른 사람 풀이 참고)
# from collections import deque
#
# N, M = map(int, input().split())
# island = [list(input()) for _ in range(N)]
#
# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def bfs(row, col):
#     cnt = 0
#     Q = deque()
#     Q. append((row, col))
#     visited[row][col] = 1 # 0과 다르게 하려고 출발지에서는 0시간인데 여기서 1로 해놨으니,
#     while Q:
#         sr, sc = Q.popleft()
#         for i in range(4):
#             nr = sr + d[i][0]
#             nc = sc + d[i][1]
#             if 0 <= nr < N and 0 <= nc < M:
#                 if island[nr][nc] == 'L' and visited[nr][nc] == 0:
#                     Q.append((nr, nc))
#                     visited[nr][nc] = visited[sr][sc] + 1 # 몇시간 왔나 세기
#                     if visited[nr][nc] > cnt:
#                         cnt = visited[nr][nc]
#     return cnt - 1 # 여기서 1을 빼줘야 온 시간이 계산됨
#
#
# result = []
# for r in range(N):
#     for c in range(M):
#         if island[r][c] == 'L':
#             count = 0
#             for k in range(4):
#                 ni, nj = r + d[k][0], c + d[k][1]
#                 if 0 <= ni < N and 0 <= nj < M and island[ni][nj] == 'L':
#                     count += 1
#             if count > 2:
#                 continue
#             else:
#                 visited = [[0] * M for _ in range(N)]  # 매번 출발할 때마다 초기화~
#                 result.append(bfs(r, c))
#
# print(max(result))

"""
시간 초과 나지 않은 다른사람 코드 2
BFS로 최솟값을 구하지만 문제는 시작 노드를 어떻게 판별하는가?
시작 노드는 leaf노드여야한다. => 
"""

'''
from collections import deque
R, C = map(int, input().split())
M = []

dy = [-1, 1, 0, 0]  # 상하 좌우
dx = [0, 0, -1, 1]
L = []
for i in range(R):
    tmp = list(input())
    M.append(tmp)


def DFS(start, visited):
    s = [start]
    tmp = []
    while s:
        y, x = s.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if M[ny][nx] == 'W' and visited[ny][nx] == 0:
                    s.append((ny, nx))
                    visited[ny][nx] = 1
                elif M[ny][nx] == 'L':
                    tmp.append((ny, nx))
    return tmp


wvisited = [[0 for i in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        if M[i][j] == 'L':
            if i == 0 or j == 0:
                L.append((i, j))
        # 바다에 접한 친구들넣기
        elif M[i][j] == 'W' and wvisited[i][j] == 0:
            L += DFS([i, j], wvisited)
L = list(set(L))


def BFS(leaf):
    q = deque([leaf])

    visited = [[0 for i in range(C)] for i in range(R)]
    visited[leaf[0]][leaf[1]] = 1
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < R and 0 <= nx < C and M[ny][nx] == 'L' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
    return time


answer = 0
# 리프부터 돌면서 BFS
for leaf in L:
    answer = max(answer, BFS(leaf))
print(answer)
'''