import sys

n = int(sys.stdin.readline())

def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    print(LCM(a, b))