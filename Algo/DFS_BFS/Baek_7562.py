import sys
from collections import deque

t = int(sys.stdin.readline())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, -2, 2, -1, 1]


def bfs(x, y):
    que = deque()
    que.append((x, y, 0))
    board[y][x] = False

    while que:
        tx, ty, cnt = que.popleft()

        if tx == target_x and ty == target_y:
            return cnt

        for i in range(8):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if nx < 0 or nx >= boardSize or ny < 0 or ny >= boardSize:
                continue

            if board[ny][nx]:
                board[ny][nx] = False
                que.append((nx, ny, cnt + 1))

for _ in range(t):
    boardSize = int(sys.stdin.readline())
    board = [[True for _ in range(boardSize)] for _ in range(boardSize)]
    start_x, start_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())

    print(bfs(start_x, start_y))