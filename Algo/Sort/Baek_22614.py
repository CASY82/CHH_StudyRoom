import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == m == 0:
        break

    tmp = []
    infected = [0] * n
    infected[0] = 1

    for i in range(m):
        t, s, d = map(int, sys.stdin.readline().split())

        tmp.append([t, s, d])

    tmp.sort(key=lambda x: x[0])

    for j in range(m):
        if infected[tmp[j][1] - 1] == 1:
            infected[tmp[j][2] - 1] = 1

    print(infected.count(1))