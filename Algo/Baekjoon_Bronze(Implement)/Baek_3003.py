chess = [int(x) for x in input().strip().split()]
white_chess = [1, 1, 2, 2, 2, 8]
result = []

for i in range(6):
    result.append(white_chess[i] - chess[i])

for j in result:
    print(j, end=' ')