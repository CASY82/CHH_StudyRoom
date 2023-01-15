import sys

n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))

house.sort(reverse=True)
time = 0

if house[0] > 1440:
    print(-1)
else:
    while house:
        if len(house) > 1:
            time += 1
            house[0] -= 1
            house[1] -= 1
        elif len(house) == 1:
            time += 1
            house[0] -= 1

        house.sort(reverse=True)
        while house and house[-1] == 0:
            house.pop()

    if time <= 1440:
        print(time)
    else:
        print(-1)