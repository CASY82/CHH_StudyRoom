import sys

n = int(sys.stdin.readline())

for i in range(n):
    length = list(map(int, sys.stdin.readline().split()))

    length.sort()

    print("Scenario #{0}:".format(i+1))
    if length[0] ** 2 + length[1] ** 2 == length[2] ** 2:
        print("yes")
    else:
        print("no")

    print()