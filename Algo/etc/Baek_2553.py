import sys

n = int(sys.stdin.readline())

tmp = 1

for cnt in range(2, n+1):
    tmp *= cnt

    while tmp % 10 == 0:
        tmp //= 10

    tmp %= 10000000

print(tmp%10)