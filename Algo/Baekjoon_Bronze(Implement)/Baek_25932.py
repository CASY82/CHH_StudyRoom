import sys

n = int(sys.stdin.readline())

for _ in range(n):
    uniform_set = list(map(int, sys.stdin.readline().split()))

    mack = False
    zack = False

    for num in uniform_set:
        if num == 18:
            mack = True

        if num == 17:
            zack = True

    print(*uniform_set)
    if mack and zack:
        print("both")
    elif mack:
        print("mack")
    elif zack:
        print("zack")
    else:
        print("none")

    print()