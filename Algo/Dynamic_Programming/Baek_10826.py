import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())

num = [0, 1] + [0] * (n+1)

def fibo(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    if num[n] != 0:
        return num[n]

    num[n] = fibo(n-1) + fibo(n-2)
    return num[n]

print(fibo(n))