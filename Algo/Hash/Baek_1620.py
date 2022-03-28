import sys

n, m = map(int, sys.stdin.readline().split())
poketmon_num = dict()
poketmon_name = dict()

for i in range(n):
    name = sys.stdin.readline().strip()
    poketmon_num[i+1] = name
    poketmon_name[name] = (i + 1)

for j in range(m):
    answer = sys.stdin.readline().strip()

    try:
        print(poketmon_num[int(answer)])
    except:
        print(poketmon_name[answer])