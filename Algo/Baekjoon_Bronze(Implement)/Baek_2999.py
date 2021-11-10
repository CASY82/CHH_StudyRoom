message = input()

divisorsList = []
n = len(message)

for i in range(1, int(n ** (1 / 2)) + 1):
    if (n % i == 0):
        divisorsList.append(i)

divisorsList.sort()
r = divisorsList[len(divisorsList) - 1]
c = n // r

array = [[' ' for i in range(c)] for j in range(r)]
count = 0

for i in range(c):
    for j in range(r):
        array[j][i] = message[count]
        count += 1

for i in range(r):
    for j in range(c):
        print(array[i][j], end='')