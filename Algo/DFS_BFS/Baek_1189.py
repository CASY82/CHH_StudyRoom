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