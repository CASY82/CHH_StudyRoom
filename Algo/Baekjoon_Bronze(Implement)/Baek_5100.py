import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    joe = jean = jane = james = nope = 0

    for _ in range(n):
        cloth = sys.stdin.readline().strip()

        if cloth == 'M' or cloth == 'L':
            joe += 1
        elif cloth == 'S':
            james += 1
        elif cloth == 'X':
            nope += 1
        elif int(cloth) >= 12:
            jean += 1
        elif int(cloth) < 12:
            jane += 1

    print(joe, jean, jane, james, nope)