import sys

board = []

for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

r, c = map(int, sys.stdin.readline().split())

# r = y / c = x
# -1 : 장애물 / 1 : 사과
apple = []
result = [0]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def backtrack(x, y, n):
    if n == 4:
        if apple.count(1) >= 2:
           result[0] = 1

        return

    else:
        if board[y][x] != -1:
            for i in range(4):
                lx = x + dx[i]
                ly = y + dy[i]

                if 0 <= lx < 5 and 0 <= ly < 5:
                    if board[y][x] == 1:
                        apple.append(1)
                        origin = 1
                    else:
                        apple.append(0)
                        origin = 0

                    board[y][x] = -1
                    backtrack(lx, ly, n + 1)
                    board[y][x] = origin
                    apple.pop()

backtrack(c, r, 0)
print(result[0])