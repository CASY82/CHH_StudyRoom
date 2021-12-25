import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sick = list(sys.stdin.readline().strip().split())
    num = float(sick[0])

    for i in range(1, len(sick)):
        if sick[i] == "@":
            num *= 3

        if sick[i] == "%":
            num += 5

        if sick[i] == "#":
            num -= 7

    print('%0.2f' % float(num))