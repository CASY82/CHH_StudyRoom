import sys

n, m = map(int, sys.stdin.readline().split())

girlgroup = dict()
girllist = dict()

for _ in range(n):
    group_name = sys.stdin.readline().strip()
    group_memeber = []
    size = int(sys.stdin.readline())

    for _ in range(size):
        girl_name = sys.stdin.readline().strip()
        group_memeber.append(girl_name)
        girllist[girl_name] = group_name

    group_memeber.sort()

    girlgroup[group_name] = group_memeber

# quiz
for _ in range(m):
    sol = sys.stdin.readline().strip()
    type = int(sys.stdin.readline())

    if type == 1:
        print(girllist[sol])
    else:
        for i in range(len(girlgroup[sol])):
            print(girlgroup[sol][i])