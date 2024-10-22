import sys

t = int(sys.stdin.readline())

for i in range(t):
    name = sys.stdin.readline().strip()
    first = sys.stdin.readline().strip()

    print("Case {0}: {1}, {2}".format(i + 1, first, name))