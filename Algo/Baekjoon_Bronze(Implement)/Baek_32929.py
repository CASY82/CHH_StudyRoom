import sys

n = int(sys.stdin.readline())

if n % 3 == 1:
    print("U")
elif n % 3 == 2:
    print("O")
elif n % 3 == 0:
    print("S")