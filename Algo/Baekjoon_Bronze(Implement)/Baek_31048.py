import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())

    if num < 5:
        tmp = 1
        for i in range(1, num + 1):
            tmp *= i

        print(tmp % 10)
    else:
        print(0)