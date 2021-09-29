n = int(input())
mine = []
result = [[0 for i in range(n)] for j in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    mine.append(list(input()))


for i in range(n):
    for j in range(n):
        if mine[i][j] != '.':
            result[i][j] = '*'
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]

                if x < 0 or y < 0 or x >= n or y >= n:
                    continue

                if result[x][y] == '*':
                    continue

                result[x][y] += int(mine[i][j])

for i in range(n):
    for j in range(n):
        if result[i][j] != '*':
            if result[i][j] >= 10:
                result[i][j] = 'M'

        print(result[i][j], end='')
    print()

'''
2
1.
.4
'''