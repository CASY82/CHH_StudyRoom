import sys

n, m = map(int, sys.stdin.readline().split())

bread = []

for _ in range(n):
    tmp = list(sys.stdin.readline().strip())
    tmp.reverse()

    bread.append(tmp)

for i in range(n):
    for j in range(m):
        print(bread[i][j], end='')
    print()