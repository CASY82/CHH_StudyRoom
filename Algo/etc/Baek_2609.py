import sys
a, b = map(int, sys.stdin.readline().split())

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

print(GCD(a, b))
print((a * b) // GCD(a, b))