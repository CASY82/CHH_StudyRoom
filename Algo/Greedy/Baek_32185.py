import sys

n, m = map(int, sys.stdin.readline().split())

jaewon_sum = sum(list(map(int, sys.stdin.readline().split())))
vol_sum = []
res = [0]

for i in range(1, n + 1):
    volunteer_sum = sum(list(map(int, sys.stdin.readline().split())))

    vol_sum.append([i, volunteer_sum])

vol_sum.sort(key=lambda x:-x[1])

for val in vol_sum:
    if jaewon_sum >= val[1] and len(res) < m:
        res.append(val[0])

    if len(res) >= m:
        break

print(*res)