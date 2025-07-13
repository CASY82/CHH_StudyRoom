import sys

n = int(sys.stdin.readline())

mabangjin = []
res = True

for _ in range(n):
    mabangjin.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(n):
        if mabangjin[i][j] != mabangjin[j][i]:
            res = False
            break

    if not res:
        break

if res:
    print("YES")
else:
    print("NO")