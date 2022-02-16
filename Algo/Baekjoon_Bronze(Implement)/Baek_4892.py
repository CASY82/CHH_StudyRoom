import sys
i = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    n *= 3
    tmp = n
    if n % 2 == 0:
        n //= 2
    else:
        n = (n+1) // 2

    n *= 3
    n //= 9

    if tmp % 2 == 0:
        # n *= 2
        print(i,". even ", n, sep="")
    else:
        # n = n * 2 + 1
        print(i,". odd ", n, sep="")

    i += 1