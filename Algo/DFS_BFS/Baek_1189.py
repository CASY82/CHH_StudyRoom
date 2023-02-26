import sys

r, c, k = map(int, sys.stdin.readline().split())

loc = []
result = [0]
visited = [[True for _ in range(c)] for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    loc.append(list(sys.stdin.readline().strip()))

def backtrack(x, y, n):
    if n == k and x == c-1 and y == 0:
        result[0] += 1

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < r:
                if visited[ny][nx] and loc[ny][nx] != 'T':
                    visited[ny][nx] = False
                    backtrack(nx, ny, n + 1)
                    visited[ny][nx] = True

visited[r-1][0] = False
backtrack(0, r-1, 1)
print(result[0])


# 다른사람 코드

# import sys
# r,c,K = map(int,sys.stdin.readline().split())
# l=[]
# for i in range(r):
#     l.append(list(map(str,sys.stdin.readline().strip("\n"))))
# v=[[0]*c for _ in range(r)]
# cnt=0
#
# def check(y,x,k):
#     global cnt
#     if k==K:
#         if (y,x)==(0,c-1):
#             cnt=cnt+1
#     else:
#         v[y][x]=1
#         for i in range(4):
#             dy=[1,0,-1,0]
#             dx=[0,1,0,-1]
#             ny=y+dy[i]
#             nx=x+dx[i]
#             if 0<=ny<r and 0<=nx<c and v[ny][nx]==0 and l[ny][nx] != "T":
#                 v[ny][nx]=1
#                 check(ny,nx,k+1)
#                 v[ny][nx]=0
#
# v[r-1][0]=1
# check(r-1,0,1)
# print(cnt)