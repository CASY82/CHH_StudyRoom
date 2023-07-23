import sys

n, m = map(int, sys.stdin.readline().split())

board = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = board[0][0]
        elif i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + board[i][j]
        elif i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j] + board[i][j]
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + board[i][j] - dp[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1 - 1])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1 - 1][y2])
    else:
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])


# 다른 사람 풀이
# import sys
# input=sys.stdin.readline
#
# n,m=map(int,input().split())
# a=[[0]*(n+1)]
#
# dp=[[0]*(n+1) for i in range(n+1)]
#
# for i in range(n):
#     a.append([0]+[i for i in map(int, input().split())])
#
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+a[i][j]
#
# for i in range(m):
#     x1,y1,x2,y2=map(int,input().split())
#     result=dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
#     print(result)