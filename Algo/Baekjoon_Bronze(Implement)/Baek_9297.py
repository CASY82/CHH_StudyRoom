import sys

t = int(sys.stdin.readline())

for i in range(1, t + 1):
    parent, child = map(int, sys.stdin.readline().split())

    mock = parent // child
    remain = parent % child

    if remain != 0 and mock != 0:
        print("Case {0}: {1} {2}/{3}".format(i, mock, remain, child))
    elif remain == 0:
        print("Case {0}: {1}".format(i, mock))
    elif mock == 0:
        print("Case {0}: {1}/{2}".format(i, remain, child))