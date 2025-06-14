import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
tmp = (b % 12)

if (a + tmp) > 12:
    print(a + tmp - 12)
else:
    print(a + tmp)