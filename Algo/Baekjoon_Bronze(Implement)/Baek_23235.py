import sys

case = 1

while True:
    num_list = list(map(int, sys.stdin.readline().split()))

    if num_list[0] == 0:
        break

    print("Case {}: Sorting... done!".format(case))

    case += 1