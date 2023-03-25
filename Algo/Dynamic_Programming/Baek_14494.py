import sys

n, m = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(n)] for _ in range(m)]

dx = [1, 1, 0]
dy = [0, 1, 1]

def dp(x, y):
    for num in range(3):
        nx = x - dx[num]
        ny = y - dy[num]

        if 0 <= nx < n and 0 <= ny < m:
            arr[y][x] = (arr[y][x] + arr[ny][nx]) % 1000000007

        arr[y][x] %= 1000000007

arr[0][0] = 1

for i in range(m):
    for j in range(n):
        dp(j, i)

print(arr[m-1][n-1])

# 다른사람 풀이
# n, m = map(int, input().split())
# dp = [[0] * 1001 for _ in range(1001)]
# dp[1][1] = 1
# for x in range(1, n + 1):
#     for y in range(1, m + 1):
#         if x == 1 and y == 1:
#             continue
#         dp[x][y] = (dp[x - 1][y - 1] + dp[x][y - 1] + dp[x - 1][y]) % (10 ** 9 + 7)
#
# print(dp[x][y])