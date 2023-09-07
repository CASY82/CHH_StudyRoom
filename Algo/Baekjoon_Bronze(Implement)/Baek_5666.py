import sys

while True:
    try:
        h, p = map(int, sys.stdin.readline().split())
    except:
        break

    print("%.2f" % (h/p))