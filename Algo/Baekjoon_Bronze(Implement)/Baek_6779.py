import sys

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())

t = 1
check = False

while t <= m:
    if -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t < 0:
        check = True
        break

    t += 1

if check:
    print("The balloon first touches ground at hour: {}".format(t))
else:
    print("The balloon does not touch ground in the given time.")