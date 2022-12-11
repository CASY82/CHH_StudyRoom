import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num, bit = map(int, sys.stdin.readline().split())

    tmp = format(num, 'b')
    if tmp.count('1') % 2 == 0 and bit == 0:
        print("Valid")
    elif tmp.count('1') % 2 == 1 and bit == 1:
        print("Valid")
    else:
        print("Corrupt")