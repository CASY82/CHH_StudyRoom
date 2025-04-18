import sys

n = int(sys.stdin.readline())

for case in range(1, n + 1):
    m = int(sys.stdin.readline())

    tmp = []

    for _ in range(m):
        tmp.append(int(sys.stdin.readline()) + 1)

    print("Case {}:".format(case))
    for i in range(m):
        if tmp[i] <= 6:
            print(tmp[i])