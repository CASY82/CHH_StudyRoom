import sys

def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

x, y = map(int, sys.stdin.readline().split())

print(LCM(x, y))