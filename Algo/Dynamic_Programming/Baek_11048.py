import sys

n, m = map(int, sys.stdin.readline().split())

maze = []
tmp = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().split())))

tmp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue

        if i == 0:
            tmp[i][j] = max(tmp[i][j - 1] + maze[i][j], tmp[i][j - 1])
        elif j == 0:
            tmp[i][j] = max(tmp[i - 1][j] + maze[i][j], tmp[i - 1][j])
        else:
            tmp[i][j] = max(tmp[i - 1][j - 1] + maze[i][j], tmp[i - 1][j] + maze[i][j], tmp[i][j - 1] + maze[i][j])

print(tmp[n-1][m-1])


# 참고

# from sys import stdin
#
# input = stdin.readline
#
# R, C = map(int, input().split())
# mapp = []
# dp = [[0 for _ in range(C)] for _ in range(R)]
# for r in range(R):
#     mapp.append(list(map(int, input().split())))
#
# dp[0][0] = mapp[0][0]
# for r in range(1,R):
#     dp[r][0] = mapp[r][0] + dp[r-1][0]
# for c in range(1,C):
#     dp[0][c] = mapp[0][c] + dp[0][c-1]
#
# for r in range(1,R):
#     for c in range(1,C):
#         dp[r][c] = max(dp[r-1][c] + mapp[r][c], dp[r][c-1] + mapp[r][c])
#
# print(dp[R-1][C-1])