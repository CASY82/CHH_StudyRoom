import sys

def round_to_first_digit(number):
    return int(number * 10 + 0.5) / 10

t = int(sys.stdin.readline())

for _ in range(t):
    p, q = map(int, sys.stdin.readline().split())

    f = (1 / p) + (1 / q)

    print("f = {}".format(round_to_first_digit(1 / f)))