import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    num = list(map(int, sys.stdin.readline().split()))

    mary = num.count(0)
    john = num.count(1)

    print("Mary won {0} times and John won {1} times".format(mary, john))