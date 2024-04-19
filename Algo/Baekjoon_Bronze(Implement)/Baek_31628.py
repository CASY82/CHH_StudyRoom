import sys

board = []
result = False

for _ in range(10):
    board.append(list(sys.stdin.readline().strip().split()))

for i in range(10):
    if board[i].count(board[i][0]) == 10:
        result = True

zip_board = list(zip(*board))

for i in range(10):
    if zip_board[i].count(zip_board[i][0]) == 10:
        result = True

if result:
    print(1)
else:
    print(0)