import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    max_num = n

    while True:
        if n == 1:
            break

        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

        if max_num < n:
            max_num = n

    print(max_num)