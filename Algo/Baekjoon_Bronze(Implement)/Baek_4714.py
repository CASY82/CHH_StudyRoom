import sys

while True:
    n = float(sys.stdin.readline())

    if n < 0:
        break

    tmp = n * 0.167

    print("Objects weighing {0:.2f} on Earth will weigh {1:.2f} on the moon.".format(n, tmp))