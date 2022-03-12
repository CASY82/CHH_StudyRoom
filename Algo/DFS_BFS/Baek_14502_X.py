# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# laboratory = []
#
# for _ in range(n):
#     laboratory.append(list(map(int, sys.stdin.readline().split())))
#
#
# # 일단 벽을 세울 위치를 완전 탐색으로 지정
# # 벽이 세워지면 dfs
#
# def dfs(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#
#     if laboratory[y][x] == 2:
#         dfs(x + 1, y)
#         dfs(x - 1, y)
#         dfs(x, y + 1)
#         dfs(x, y - 1)
#         return True
#
#     return False

# 백트래킹과 BFS의 합작품 해당 문제는 참고하여 풀었다. pypy로 통과
import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
laboratory = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = [0]

for _ in range(n):
    laboratory.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    que = deque()
    tmp = copy.deepcopy(laboratory)
    #아무래도 이것때문에 시간초과가 발생하는듯 해당 부분을 저장하여 진행하도록 해야 초과가 안날듯 싶다.
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                que.append((j, i))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or ny >= n or nx >= m:
                continue

            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                que.append((nx, ny))

    cnt = 0

    for i in range(n):
        cnt += tmp[i].count(0)

    result[0] = max(result[0], cnt)

def backtrack(v):
    if v == 3:
        bfs()
        return

    else:
        for i in range(n):
            for j in range(m):
                if laboratory[i][j] == 0:
                    laboratory[i][j] = 1
                    backtrack(v + 1)
                    laboratory[i][j] = 0

backtrack(0)

print(result[0])

# 내가 제출한 예제는 python은 시간 초과 pypy로만 통과함
# from sys import stdin
# from typing import List
# from itertools import combinations
# from collections import deque
#
#
# lab, viruses, blanks = [], [], []
# n, m = 0, 0
# dy = [1, -1, 0, 0]
# dx = [0, 0, 1, -1]
#
#
# def bfs(y: int, x: int, lab_copy: List[List[int]]) -> None:
#     dq = deque([(y, x)])
#     while dq:
#         cy, cx = dq.popleft()
#         for i in range(4):
#             ny, nx = cy + dy[i], cx + dx[i]
#             if 0 <= ny < n and 0 <= nx < m and lab_copy[ny][nx] == 0:
#                 lab_copy[ny][nx] = 2
#                 dq.append((ny, nx))
#
#
# def main():
#     def input():
#         return stdin.readline().rstrip()
#     global lab, viruses, n, m
#
#     n, m = map(int, input().split())
#     lab = [list(map(int, input().split())) for _ in range(n)]
#
#     # 바이러스, 빈 공간 위치 저장
#     for i in range(n):
#         for j in range(m):
#             if lab[i][j] == 2:
#                 viruses.append((i, j))
#             elif lab[i][j] == 0:
#                 blanks.append((i, j))
#
#     res = 0
#     # 벽 세우기
#     combs = combinations(blanks, 3)
#     for comb in combs:
#         lab_copy = [row[:] for row in lab]
#         for y, x in comb:
#             lab_copy[y][x] = 1
#         # 벽 3개 다 세우면 바이러스 확산
#         for y, x in viruses:
#             bfs(y, x, lab_copy)
#         # 안전 지대 개수 구하기
#         safezone = sum(i.count(0) for i in lab_copy)
#         res = max(safezone, res)
#
#     print(res)
#
#
# if __name__ == "__main__":
#     main()

# 다른 예제
# import sys
# from collections import deque
# import copy
#
# def findvirus(maps,n,m,visit):
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] == 2 and visit[i][j] == 0:
#                 #print(i,j)
#                 return i,j
#     return 10,10
#
# def bfs(maps,n,m):
#     q = deque()
#     visit = [[0 for _ in range(m)] for _ in range(n)]
#     vx,vy = findvirus(maps,n,m,visit) # vx, vy는 바이러스의 첫 위치
#     q.append((vx,vy))
#     #print("vx,vy",vx,vy)
#     visit[vx][vy] = 1
#
#     while q:
#         (x,y) = q.popleft()
#         for (dx,dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
#             (nx,ny) = (x+dx, y+dy)
#             if 0<= nx < n and 0<= ny < m and visit[nx][ny] == 0:
#                 visit[nx][ny] = 1
#                 #print("nx,ny",nx,ny)
#                 #print("visit", visit[-1][-1])
#                 if maps[nx][ny] == 0:
#                     maps[nx][ny] = 2
#                     q.append((nx,ny))
#                 elif maps[nx][ny] == 1:
#                     tx,ty = findvirus(maps,n,m,visit)
#                     #print("tx,ty",tx,ty)
#                     if (tx,ty) != (10,10):
#                         visit[tx][ty] = 1
#                         q.append((tx,ty))
#                 else:
#                     q.append((nx,ny))
#     cnt = 0
#     for map in maps:
#         #print(map)
#         cnt += map.count(0)
#     #print("cnt", cnt)
#     #for v in visit:
#         #print(v)
#     return cnt
#
#
# n,m = map(int,sys.stdin.readline().rstrip().split())
# maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
# coordinate = []
# for i in range(n):
#     for j in range(m):
#         coordinate.append((i,j))
# #print(maps)
# safezones = 0
# cnt = 0
# for (a1,a2) in coordinate:
#     if maps[a1][a2] == 0:
#         for (b1,b2) in coordinate[a1*m+a2+1:]:
#             if maps[b1][b2] == 0:
#                 for (c1,c2) in coordinate[b1*m+b2+1:]:
#                     #print((a1,a2),(b1,b2),(c1,c2))
#                     if maps[c1][c2] == 0:
#                         cnt+=1
#                         case = copy.deepcopy(maps)
#                         case[a1][a2], case[b1][b2], case[c1][c2] = 1,1,1
#                         t = bfs(case,n,m)
#                         if t > safezones:
#                             safezones = t
# print(safezones)
# #print(cnt)
