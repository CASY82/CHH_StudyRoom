#상하좌우

n = int(input())
move_plan = list(input().split())

move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 1
y = 1

for a in move_plan:
    for i in range(len(move)):
        if a == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx > n or nx < 1 or ny > n or nx < 1:
        continue

    x, y = nx, ny


print(x, y)

