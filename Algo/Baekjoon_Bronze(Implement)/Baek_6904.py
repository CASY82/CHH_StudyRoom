import sys

while True:
    n = int(sys.stdin.readline())
    minimal = 1000000000000
    min_i = 0
    min_another = 0

    if n == 0:
        break

    for i in range(1, n+1):
        if n == i * (n//i):
            tmp = i*2 + (n//i)*2
            if minimal > tmp:
                minimal = tmp
                min_i = i
                min_another = n//i

    print("Minimum perimeter is {0} with dimensions {1} x {2}".format(minimal, min(min_i, min_another), max(min_i, min_another)))