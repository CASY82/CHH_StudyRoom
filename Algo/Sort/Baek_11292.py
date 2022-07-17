import sys

while True:
    n = int(sys.stdin.readline())
    heightL = []

    if n == 0:
        break

    for _ in range(n):
        name, height = sys.stdin.readline().strip().split()
        height = float(height)
        heightL.append([name, height])

    heightL.sort(key = lambda x : -x[1])

    max = heightL[0][1]

    for i in heightL:
        if i[1] == max:
            print(i[0], end=' ')

    print()