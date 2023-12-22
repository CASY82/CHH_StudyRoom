import sys

n = int(sys.stdin.readline())

dots = []
result = 0

for _ in range(n):
    loc, color = map(int, sys.stdin.readline().split())

    dots.append((loc, color))

dots.sort(key=lambda x: (x[1], x[0]))

for dot in range(len(dots)):
    tmp = 0
    if dot == 0:
        tmp += abs(dots[dot + 1][0] - dots[dot][0])
    elif dot == len(dots) - 1:
        tmp += abs(dots[dot][0] - dots[dot - 1][0])
    else:
        if dots[dot][1] == dots[dot + 1][1] and dots[dot][1] == dots[dot - 1][1]:
            tmp += min(abs(dots[dot + 1][0] - dots[dot][0]), abs(dots[dot][0] - dots[dot - 1][0]))
        elif dots[dot][1] == dots[dot + 1][1] and dots[dot][1] != dots[dot - 1][1]:
            tmp += abs(dots[dot + 1][0] - dots[dot][0])
        elif dots[dot][1] != dots[dot + 1][1] and dots[dot][1] == dots[dot - 1][1]:
            tmp += abs(dots[dot][0] - dots[dot - 1][0])

    result += tmp

print(result)