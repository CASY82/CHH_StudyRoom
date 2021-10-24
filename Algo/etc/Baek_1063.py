king, stone, n = input().split()
n = int(n)

chess_board = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
moving = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

first_king = list(king)
first_stone = list(stone)

x = chess_board.index(first_king[0])
x_s = chess_board.index(first_stone[0])
y = int(first_king[1]) - 1
y_s = int(first_stone[1]) - 1

for _ in range(n):
    move = input()


    if x + dx[moving.index(move)] == x_s and y + dy[moving.index(move)] == y_s:
        if x_s + dx[moving.index(move)] < 0 or y_s + dy[moving.index(move)] < 0 or x_s + dx[moving.index(move)] >= 8 or y_s + dy[moving.index(move)] >= 8:
            continue

        x_s = x_s + dx[moving.index(move)]
        y_s = y_s + dy[moving.index(move)]
        x = x + dx[moving.index(move)]
        y = y + dy[moving.index(move)]

    else:
        if x + dx[moving.index(move)] < 0 or y + dy[moving.index(move)] < 0 or x + dx[moving.index(move)] >= 8 or y + dy[moving.index(move)] >= 8:
            continue

        x = x + dx[moving.index(move)]
        y = y + dy[moving.index(move)]

print(chess_board[x] + str(y + 1))
print(chess_board[x_s] + str(y_s + 1))