import sys

INF = int(1e9)

v, e = map(int, sys.stdin.readline().split())

load = [[INF] * (v + 1) for _ in range(v + 1)]
result = int(1e9)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())

    load[a][b] = c

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            load[a][b] = min(load[a][b], load[a][k] + load[k][b])

for a in range(1, v + 1):
    if result > load[a][a]:
        result = load[a][a]

if result >= int(1e9):
    print(-1)
else:
    print(result)