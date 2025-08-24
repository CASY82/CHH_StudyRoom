import sys

n, k = map(int, sys.stdin.readline().split())

data = []

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    tmp = []
    for j in range(n):
        for _ in range(k):
            print(data[i][j], end=" ")
            tmp.append(str(data[i][j]))
    print()
    for _ in range(k - 1):
        print(*tmp)