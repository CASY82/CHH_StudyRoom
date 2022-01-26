import sys

n, k = map(int, sys.stdin.readline().split())
nation = []
rank = [0] * n

for _ in range(n):
    nation.append(list(map(int, sys.stdin.readline().split())))

nation.sort(key= lambda x:(x[1], x[2], x[3]), reverse=True)

rankCnt = 1
adder = 0
data = [0, 0, 0]
for i in nation:
    if data[0] != i[1] or data[1] != i[2] or data[2] != i[3]:
        rankCnt += adder
        adder = 0

    data[0] = i[1]
    data[1] = i[2]
    data[2] = i[3]
    rank[i[0] - 1] = rankCnt
    adder += 1

print(rank[k-1])