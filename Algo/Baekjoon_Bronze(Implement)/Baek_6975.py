import sys

n = int(sys.stdin.readline())

for case in range(n):
    num = int(sys.stdin.readline())

    tmp = set()

    for i in range(1, num + 1):
        if num % i == 0:
            tmp.add(i)

    if sum(tmp) - num < num:
        print("{} is a deficient number.".format(num))
    elif sum(tmp) - num == num:
        print("{} is a perfect number.".format(num))
    elif sum(tmp) - num > num:
        print("{} is an abundant number.".format(num))
    print()