import sys

n, m = map(int, sys.stdin.readline().split())
area = []

for i in range(n):
    area.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue

        tmp = 0

        if area[i][j] == 1:
            tmp += 1

        if i == 0:
            area[i][j] = area[i][j-1] + tmp
        elif j == 0:
            area[i][j] = area[i-1][j] + tmp
        else:
            area[i][j] = max(area[i-1][j] + tmp,  area[i][j-1] + tmp)

print(area[n-1][m-1])

# 다른사람 코드 참조(비슷허네~)
# N, M = map(int, input().split())
#
#
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         if i == 0 and j != 0:
#             arr[i][j] += arr[i][j-1]
#         if i != 0 and j == 0:
#             arr[i][j] += arr[i-1][j]
#         if i != 0 and j != 0:
#             arr[i][j] = max(arr[i-1][j], arr[i][j-1]) + arr[i][j]
#
# print(max(map(max, arr)))