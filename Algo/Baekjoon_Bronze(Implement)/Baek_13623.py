import sys

a, b, c = map(int, sys.stdin.readline().split())

if a + b + c == 3 or a + b + c == 0:
    print("*")
else:
    if a != b and a != c:
        print("A")
    elif b != a and b != c:
        print("B")
    elif c != a and c != b:
        print("C")