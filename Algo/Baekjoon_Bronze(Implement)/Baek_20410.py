import sys

m, seed, x1, x2 = map(int, sys.stdin.readline().split())
res = []
check = False

for i in range(2, m + 1):
    for j in range(2, m + 1):
        if x1 == (i * seed + j) % m and x2 == (i * x1 + j) % m:
            res.append(i)
            res.append(j)
            check = True
            break
    if check:
        break

print(*res)