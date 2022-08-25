import sys

n = int(sys.stdin.readline())

mirror = []

for _ in range(n):
    mirror.append(list(sys.stdin.readline().strip()))

k = int(sys.stdin.readline())

if k == 1:
    for i in range(n):
        for j in range(n):
            print(mirror[i][j], end='')
        print()
elif k == 2:
    for i in range(n):
        mirror[i].reverse()
        for j in range(n):
            print(mirror[i][j], end='')
        print()
else:
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(mirror[i][j], end='')
        print()