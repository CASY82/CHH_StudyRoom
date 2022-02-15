import sys

n, m = map(int, sys.stdin.readline().split())

if n > 2 and m < 6:
    if m == 5:
        print(4)
    else:
        print(m)
elif n > 2 and m >= 6:
    print(m-6+4)
elif n == 2 and m <= 6:
    if m % 2 == 0:
        print(m//2)
    else:
        print(m//2+1)
elif n == 2 and m > 6:
    print(4)
else:
    print(1)