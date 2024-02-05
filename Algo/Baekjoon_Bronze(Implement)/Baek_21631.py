import sys

a, b = map(int, sys.stdin.readline().split())

if b == 0:
    print(0)
elif a == 0:
    print(1)
else:
    if a < b:
        print(a + 1)
    else:
        print(b)