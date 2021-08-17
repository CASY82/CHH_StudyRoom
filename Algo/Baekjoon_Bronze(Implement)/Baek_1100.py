count = 0
#chess_board = [['.' for _ in range(8)] for _ in range(8)]
chess_board = [list(map(str, input())) for _ in range(8)]

print(chess_board)

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and chess_board[i][j] == 'F':
            count += 1
        elif i % 2 == 1 and j % 2 == 1 and chess_board[i][j] == 'F':
            count += 1

print(count)
