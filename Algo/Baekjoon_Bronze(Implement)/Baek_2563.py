import sys

dohwazi = [[0 for _ in range(101)] for _ in range(101)]

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())

    for i in range(w, w+10):
        for j in range(h, h+10):
            dohwazi[i][j] = 1

for i in range(101):
    for j in range(101):
        if dohwazi[j][i] == 1:
            result += 1

print(result)