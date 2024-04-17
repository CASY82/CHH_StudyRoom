import sys

n = int(sys.stdin.readline())
name = sys.stdin.readline().strip()
floor = int(sys.stdin.readline())

if name == "annyong":
    if floor % 2 == 1:
        print(floor)
    else:
        if n > floor:
            print(floor + 1)
        else:
            print(floor - 1)
else:
    if floor % 2 == 0:
        print(floor)
    else:
        if n > floor:
            print(floor + 1)
        else:
            print(floor - 1)