#이것도 함수로 써서 하면 코드가 절반으로 줄 수 있을거 같다.
n = int(input())
room = []

for i in range(n):
    room.append(list(input()))

row = 0
col = 0


for i in range(n):
    connect = False
    count = 0
    for j in range(n):
        if room[i][j] == '.':
            count += 1
        else:
            connect = False
            count = 0
            continue

        if count >= 2 and connect == False:
            connect = True
            row += 1
            count = 0

for i in range(n):
    connect = False
    count = 0
    for j in range(n):
        if room[j][i] == '.':
            count += 1
        else:
            connect = False
            count = 0
            continue

        if count >= 2 and connect == False:
            connect = True
            col += 1
            count = 0

print(row, col)