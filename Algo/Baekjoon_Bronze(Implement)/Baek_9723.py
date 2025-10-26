import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    a, b, c = map(int, sys.stdin.readline().split())

    length = [a, b, c]
    length.sort()

    if length[2] ** 2 == length[0] ** 2 + length[1] ** 2:
        print("Case #{}: YES".format(case))
    else:
        print("Case #{}: NO".format(case))