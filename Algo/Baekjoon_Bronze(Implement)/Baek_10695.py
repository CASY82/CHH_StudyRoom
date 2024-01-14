import sys

t = int(sys.stdin.readline())
mov = [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

for case in range(1, t + 1):
    n, r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    check = False

    for mov1, mov2 in mov:
        if r1 + mov1 == r2 and c1 + mov2 == c2:
            check = True
            break

    if check:
        print("Case {0}: YES".format(case))
    else:
        print("Case {0}: NO".format(case))