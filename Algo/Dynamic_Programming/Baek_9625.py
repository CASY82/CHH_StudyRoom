import sys

n = int(sys.stdin.readline())
num = [0, 1, 1] + [0 for _ in range(45)]

def fibo(n):
    if n == 1 or n == 2:
        return num[1]
    elif num[n] != 0:
        return num[n]
    else:
        num[n] = fibo(n-1) + fibo(n-2)

    return num[n]

fibo(45)

print(num[n-1], num[n])