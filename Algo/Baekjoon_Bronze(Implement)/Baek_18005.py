import sys

n = int(sys.stdin.readline())

if n % 2 == 1:
    print(0)
else:
    if n % 4 == 2:
        print(1)
    else:
        print(2)