import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

while x <= y:
    print('All positions change in year {}'.format(x))

    x += 60