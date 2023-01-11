import sys

k = int(sys.stdin.readline())

for dataset in range(k):
    m, n = map(int, sys.stdin.readline().split())

    database = []
    result = 0

    for _ in range(m):
        database.append(int(sys.stdin.readline()))

    for _ in range(n):
        h, w, d, i = map(int, sys.stdin.readline().split())

        result += h * w * d * database[i-1]

    print("Data Set {}:".format(dataset+1))
    print(result)
