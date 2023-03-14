import sys

t = int(sys.stdin.readline())

gather = "a e i o u".split(" ")

for cnt in range(t):
    city = sys.stdin.readline().strip()

    if city[-1] in gather:
        print("Case #{0}: {1} is ruled by a queen.".format(cnt + 1, city))
    elif city[-1] == "y":
        print("Case #{0}: {1} is ruled by nobody.".format(cnt + 1, city))
    else:
        print("Case #{0}: {1} is ruled by a king.".format(cnt + 1, city))