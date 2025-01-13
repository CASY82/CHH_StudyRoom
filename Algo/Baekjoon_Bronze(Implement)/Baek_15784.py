import sys

n, a, b = map(int, sys.stdin.readline().split())
seat = []
a -= 1
b -= 1

for i in range(n):
    seat.append(list(map(int, sys.stdin.readline().split())))

res = True

for j in range(n):
    if seat[j][b] > seat[a][b]:
        res = False
        break

for k in range(n):
    if seat[a][k] > seat[a][b]:
        res = False
        break

if res:
    print("HAPPY")
else:
    print("ANGRY")