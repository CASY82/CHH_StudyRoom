import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c = int(sys.stdin.readline())

    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    if c >= 25:
        quarter = c // 25
        c %= 25

    if c >= 10:
        dime = c // 10
        c %= 10

    if c >= 5:
        nickel = c // 5
        c %= 5

    if c >= 1:
        penny = c

    print(quarter, dime, nickel, penny)
