r, c = map(int, input().split())
move_plan = list(input().split())

move = ['L', 'R', 'U', 'D']
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

board = []

for i in range(r):
    board.append(list(input().split()))

x = 0
y = 0

print(board)

for a in move_plan:
    for i in range(len(move)):
        if a == move[i]:
            nx = x + dr[i]
            ny = y + dc[i]

    if board[x][y] == '#':
        continue

    x, y = nx, ny


print(x, y)
