import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    tmp_tuple = list(map(int, sys.stdin.readline().split()))
    duplicate_check = set()

    duplicate_check.add(tuple(tmp_tuple))
    next_tuple = tuple(tmp_tuple)

    while True:
        tmp = ()

        for i in range(n - 1):
            tmp = tmp + (abs(next_tuple[i] - next_tuple[i + 1]),)

        tmp = tmp + (abs(next_tuple[-1] - next_tuple[0]),)

        next_tuple = tmp

        if tmp == tuple(0 for _ in range(n)):
            print("ZERO")
            break

        if tmp not in duplicate_check:
            duplicate_check.add(tmp)
        else:
            print("LOOP")
            break