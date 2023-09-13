import sys

n = int(sys.stdin.readline())

for i in range(1, 101):
    if i ** 2 <= n < (i + 1) ** 2:
        print("The largest square has side length {}.".format(i))