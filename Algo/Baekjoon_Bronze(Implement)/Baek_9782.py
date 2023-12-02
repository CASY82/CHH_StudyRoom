import sys

case = 1

while True:
    numbers = list(map(int, sys.stdin.readline().split()))

    if numbers[0] == 0:
        break

    check = numbers[1:]
    result = 0

    if numbers[0] % 2 == 0:
        result = (check[numbers[0]//2 - 1] + check[numbers[0]//2]) / 2
    else:
        result = check[numbers[0]//2]

    print("Case {0}: {1:.1f}".format(case, result))

    case += 1