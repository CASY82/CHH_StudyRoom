import sys

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            bus[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    bus[a-1][b-1] = min(c, bus[a-1][b-1])

def floydWarshall():
    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = bus[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp[i][j] = min(tmp[i][k] + tmp[k][j], tmp[i][j])

    return tmp

result = floydWarshall()

for i in range(n):
    for j in range(n):
        if result[i][j] == INF:
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')

    print()