import sys

n, m = map(int, sys.stdin.readline().split())
war = []
counter = [0]
resultB = 0
resultW = 0

for _ in range(m):
    war.append(list(sys.stdin.readline().strip()))

def dfs(x, y, peer):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if war[y][x] == peer:
        counter[0] += 1
        war[y][x] = 'K'
        dfs(x + 1, y, peer)
        dfs(x - 1, y, peer)
        dfs(x, y + 1, peer)
        dfs(x, y - 1, peer)
        return True

    return False

for i in range(m):
    for j in range(n):
        if dfs(j, i, 'B'):
            resultB += counter[0] * counter[0]
            counter[0] = 0

        if dfs(j, i, 'W'):
            resultW += counter[0] * counter[0]
            counter[0] = 0

print(resultW, resultB)

# cnt 하나로 해서 구현하고 싶은데 왜 잘 안되지..?
# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline
#
# def dfs(c, r, chr):
#     war[r][c] = 0
#     cnt = 1
#     for i in range(4):
#         x, y = c + dx[i], r + dy[i]
#         if 0 <= x < N and 0 <= y < M and war[y][x] == chr:
#             cnt += dfs(x, y, chr)
#     return cnt
#
# N, M = map(int, input().split())
# war = [list(input().strip()) for _ in range(M)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# w, b = 0, 0
# for i in range(M):
#     for j in range(N):
#         if war[i][j] == 'W':
#             v = dfs(j, i, 'W')
#             w += v ** 2
#         elif war[i][j] == 'B':
#             v = dfs(j, i, 'B')
#             b += v ** 2
# print(w, b)