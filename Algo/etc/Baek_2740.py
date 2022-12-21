import sys

n, m = map(int, sys.stdin.readline().split())

first = []

for _ in range(n):
    first.append(list(map(int, sys.stdin.readline().split())))

second = []

m, k = map(int, sys.stdin.readline().split())

for _ in range(m):
    second.append(list(map(int, sys.stdin.readline().split())))

result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for z in range(m):
            result[i][j] += first[i][z] * second[z][j]

for cnt in range(n):
    print(*result[cnt])