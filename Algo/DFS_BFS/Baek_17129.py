import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

land = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    land.append(list(sys.stdin.readline().strip()))

def bfs(x, y):
    que = deque()
    que.append((x, y, 0))
    land[y][x] = 'X'

    while que:
        lx, ly, cnt = que.popleft()

        for i in range(4):
            nx = lx + dx[i]
            ny = ly + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if land[ny][nx] != '1' and land[ny][nx] != 'X':
                    if land[ny][nx] == '3' or land[ny][nx] == '4' or land[ny][nx] == '5':
                        return cnt + 1

                    land[ny][nx] = 'X'
                    que.append((nx, ny, cnt + 1))

    return -1

for i in range(n):
    for j in range(m):
        if land[i][j] == '2':
            tmp = bfs(j, i)
            if tmp != -1:
                print("TAK")
                print(tmp)
            else:
                print("NIE")


# 수행시간이 더 빠른 다른 사람 풀이

# from collections import deque
# n,m = map(int,input().split())
# arr=[]
#
# for _ in range(n):
#     arr.append(input().strip())
#
#
# row=[0,0,-1,1]
# col=[1,-1,0,0]
# vis=[[-1 for _ in range(m)]for _ in range(n)]
#
# def bfs(x,y):
#     q=deque()
#     q.append((x,y))
#     vis[x][y]=0
#
#     while q:
#         x,y= q.popleft()
#         for i in range(4):
#             nex_x=x+row[i]
#             nex_y=y+col[i]
#             if 0<=nex_y<m and 0<=nex_x<n and arr[nex_x][nex_y]!='1' and vis[nex_x][nex_y]==-1:
#                 vis[nex_x][nex_y] = vis[x][y]+1
#                 q.append((nex_x,nex_y))
#                 if arr[nex_x][nex_y] == '3' or arr[nex_x][nex_y] == '4' or arr[nex_x][nex_y] == '5':
#                     print('TAK')
#                     print(vis[x][y]+1)
#                     exit()
#     else:
#         print('NIE')
#
# for a in range(n):
#     for b in range(m):
#         if arr[a][b] == '2':
#             bfs(a,b)