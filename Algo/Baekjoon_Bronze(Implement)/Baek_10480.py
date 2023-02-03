import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())

    if abs(num) % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))