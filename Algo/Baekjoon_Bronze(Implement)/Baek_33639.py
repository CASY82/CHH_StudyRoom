import sys

n, q = map(int, sys.stdin.readline().split())

names = dict()

for _ in range(n):
    name = sys.stdin.readline().strip().split()
    tmp = ""

    for i in range(len(name)):
        tmp += name[i][0]

    if tmp not in names:
        names[tmp] = name
    else:
        names[tmp] = ["ambiguous"]

for _ in range(q):
    initial = sys.stdin.readline().strip()

    if initial not in names:
        print("nobody")
    else:
        print(*names[initial])