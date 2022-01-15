import sys

n = int(sys.stdin.readline())
stu = []
nation = []

for _ in range(n):
    stu.append(list(map(int, sys.stdin.readline().split())))

stu.sort(key=lambda x: x[2], reverse=True)

for i in range(len(stu)):
    if len(nation) >= 3:
        break

    if nation.count(stu[i][0]) < 2:
        nation.append(stu[i][0])
        print(stu[i][0], stu[i][1])