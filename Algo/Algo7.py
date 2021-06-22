maze = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    maze[i] = list(map(int, input().split()))

maze[1][1] = 9
x = 1
y = 1

while True:
    if x == 9 or y == 9:
        break

    if maze[x][y] == 2:
        maze[x][y] = 9
        break


    #이 부분은 반대로 짜면된다 그럼 코드를 줄일 수 있을 듯 1이 나오는 경우를 if로 나누고 나머지를 else로 넣으면 해결됬을 문제
    if maze[x][y+1] == 0 or maze[x][y+1] == 2:
        maze[x][y] = 9
        y = y + 1
    else:
        maze[x][y] = 9
        x = x + 1


for i in range(10):
    for j in range(10):
        print(maze[i][j], end=' ')

    print()