#codeup 6096
ata = [[0 for j in range(19)] for i in range(19)]


for i in range(19):
    data[i] = list(map(int, input().split()))


num = int(input())

for i in range(num):
    x,y = map(int, input().split())
    for j in range(19):
        if data[x-1][j] == 0:
            data[x-1][j] = 1
        else:
            data[x-1][j] = 0

        if data[j][y-1] == 0:
            data[j][y-1] = 1
        else:
            data[j][y-1] = 0


for i in range(19):
    for j in range(19):
        print(data[i][j], end=' ')

    print()