import sys

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)

t = int(sys.stdin.readline())

for _ in range(t):
    num = list(map(int, sys.stdin.readline().split()))
    result = 0

    for i in range(1, len(num)):
        for j in range(i+1, len(num)):
            result += GCD(num[i], num[j])

    print(result)