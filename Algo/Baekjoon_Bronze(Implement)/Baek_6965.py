import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentense = list(sys.stdin.readline().strip().split())
    res = []

    for p in sentense:
        if len(p) == 4:
            res.append("****")
        else:
            res.append(p)

    print(*res)
    print()