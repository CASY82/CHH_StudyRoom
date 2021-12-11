import sys

t = int(sys.stdin.readline())

def GCD(a, b):
    if a % b == 0:
        return b

    else:
        return GCD(b, a % b)

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    print((a * b) // GCD(a, b))