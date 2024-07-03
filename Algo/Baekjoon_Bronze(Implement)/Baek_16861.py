import sys

n = int(sys.stdin.readline())

while True:
    sum_harshad = 0
    tmp = n

    while tmp > 0:
        sum_harshad += tmp % 10
        tmp //= 10

    if n % sum_harshad == 0:
        print(n)
        break

    n += 1