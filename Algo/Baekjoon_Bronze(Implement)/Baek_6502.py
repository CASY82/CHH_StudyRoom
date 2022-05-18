import sys

PIE = 3.14
i = 1

while True:
    try:
        r, w, l = map(int, sys.stdin.readline().split())
    except:
        break

    table = 2 * r
    pizza = (w ** 2 + l ** 2) ** 0.5

    if table >= pizza:
        print("Pizza {0} fits on the table.".format(i))
    else:
        print("Pizza {0} does not fit on the table.".format(i))

    i += 1