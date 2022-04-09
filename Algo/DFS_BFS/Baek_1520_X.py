import sys
sys.setrecursionlimit(10 ** 5)

m, n = map(int, sys.stdin.readline().split())

under_load = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(m):
    under_load.append(list(map(int, sys.stdin.readline().split())))

# 경로 지나간 횟수를 저장할 dp 리스트(-1로 초기화)
visited = [[-1] * n for _ in range(m)]

# 처음에 bfs인줄알았으나 dfs로 풀어야 하는 문제였다.
def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    # 이미 한번 다녀간 경우라면 더이상 계산 X
    if visited[y][x] != -1:
        return visited[y][x]

    visited[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if under_load[y][x] > under_load[ny][nx]:
                # 갈림길이 발생했을 때, 모든 경로의 경우의 수를 합치는 부분
                visited[y][x] += dfs(nx, ny)

    return visited[y][x]

print(dfs(0, 0))