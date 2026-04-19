# Box of Bricks
import sys

index = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    height = list(map(int, sys.stdin.readline().split()))

    tmp = sum(height) // n

    res = 0

    for i in height:
        res += abs(i - tmp)

    print("Set #{}".format(index))
    print("The minimum number of moves is {}.".format(res // 2))
    print()

    index += 1