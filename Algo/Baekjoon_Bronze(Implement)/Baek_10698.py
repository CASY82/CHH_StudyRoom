import sys

t = int(sys.stdin.readline())

for i in range(t):
    x, op, y, eq, z = sys.stdin.readline().strip().split()

    susic = x + op + y
    if eval(susic) == int(z):
        print("Case {0}: {1}".format(i+1, "YES"))
    else:
        print("Case {0}: {1}".format(i + 1, "NO"))