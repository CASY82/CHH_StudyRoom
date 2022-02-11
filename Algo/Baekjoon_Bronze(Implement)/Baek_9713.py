import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())
    sum = 0
    i = 1

    while i <= num:
        sum += i
        i += 2

    print(sum)