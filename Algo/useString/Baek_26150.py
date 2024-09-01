import sys

n = int(sys.stdin.readline())
tmp = []

for _ in range(n):
    data = list(sys.stdin.readline().strip().split())

    data[1] = int(data[1])
    data[2] = int(data[2])

    tmp.append(data)

tmp.sort(key=lambda x : x[1])
res = ""

for i in range(n):
    res += (tmp[i][0])[tmp[i][2] - 1]

print(res.upper())