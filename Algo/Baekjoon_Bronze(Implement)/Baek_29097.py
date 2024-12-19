import sys

n, m, k, a, b, c = map(int, sys.stdin.readline().split())

j = a * n
r = b * m
s = c * k

tmp = [[j, "Joffrey"], [r, "Robb"], [s, "Stannis"]]

tmp.sort(key=lambda x : (x[0], x[1]))
max_warrior = max(j, r, s)

res = []

for i in range(len(tmp)):
    if max_warrior == tmp[i][0]:
        res.append(tmp[i][1])

print(*res)