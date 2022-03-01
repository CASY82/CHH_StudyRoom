import sys

t = int(sys.stdin.readline())

def Euclid(a, b):
    if a % b == 0:
        return b

    else:
        return Euclid(b, a%b)

def LCM(x, y):
    result = (x * y) // Euclid(x, y)
    return result

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    print(LCM(a, b), Euclid(a, b))