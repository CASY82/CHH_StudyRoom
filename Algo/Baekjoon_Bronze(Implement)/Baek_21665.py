import sys

n, m = map(int, sys.stdin.readline().split())

origin = []
changer = []
result = 0

for _ in range(n):
    origin.append(list(sys.stdin.readline().strip()))

tmp = sys.stdin.readline().strip()

for _ in range(n):
    changer.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(m):
        if origin[i][j] == "W" and changer[i][j] == "W":
            result += 1
        elif origin[i][j] == "B" and changer[i][j] == "B":
            result += 1

print(result)