# 시간 초과

# n, m = map(int, input().split())
# num = []
# ranger = []
#
# for i in range(n):
#     num.append(list(map(int, input().split())))
#
# k = int(input())
# for j in range(k):
#     ranger.append(list(map(int, input().split())))
#
#
# for a in range(k):
#     sum_num = 0
#     for b in range(ranger[a][0]-1, ranger[a][2]):
#         for c in range(ranger[a][1] - 1, ranger[a][3]):
#             sum_num += num[b][c]
#
#     print(sum_num)

# DP로 풀어야 하는 문제
# 예시는 다음과 같다.

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# DP[i][j] = 1, 1부터 (i,j)까지의 부분 합
DP = [[0 for i in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])