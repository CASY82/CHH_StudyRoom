import sys

i = 1
while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b == c == 0:
        break

    if a == -1:
        result = ((c ** 2) - (b ** 2))
        target = 'a'
    elif b == -1:
        result = ((c ** 2) - (a ** 2))
        target = 'b'
    else:
        result = ((a ** 2) + (b ** 2))
        target = 'c'

    print("Triangle #", i, sep="")
    if result <= 0:
        print("Impossible.")
    else:
        print(target, "= {:.3f}".format(round(result ** 0.5, 3)))

    print()
    i += 1