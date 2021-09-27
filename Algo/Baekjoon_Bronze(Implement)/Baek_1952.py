m, n = map(int, input().split())

if n == m:
    print((n-1) * 2)
elif n > m:
    print((m-1) * 2)
elif n < m:
    print((n-1) * 2 + 1)

#다른사람 답안 참고(일일히 돌려서 확인하는 방법)
#
# n, m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
# x, y, d = 0, 0, 0
# a[0][0] = 1
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# answer = 0
#
# for i in range(1, n * m):
#     nx, ny = x + dx[d], y + dy[d]
#
#     if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
#         pass
#     else:
#         d = (d + 1) % 4
#         answer += 1
#         nx, ny = x + dx[d], y + dy[d]
#
#     x, y = nx, ny
#     a[x][y] = 1
#
# print(answer)
