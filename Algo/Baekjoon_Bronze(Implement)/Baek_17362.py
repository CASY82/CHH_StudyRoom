import sys

n = int(sys.stdin.readline())

finger = [5, 4, 3, 2, 1, 2, 3, 4]

if n <= 5:
    print(n)
else:
    tmp = (n-5) % 8

    print(finger[tmp])