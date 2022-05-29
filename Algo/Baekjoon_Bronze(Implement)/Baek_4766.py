import sys

change = float(sys.stdin.readline())
while True:
    num = float(sys.stdin.readline())

    if num == 999:
        break

    print(format(num - change, ".2f"))

    change = num