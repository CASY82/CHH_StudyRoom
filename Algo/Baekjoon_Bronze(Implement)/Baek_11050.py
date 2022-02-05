import sys
sys.setrecursionlimit(10 ** 5)

n, k = map(int, sys.stdin.readline().split())

def fact(n):
    if n == 1:
        return 1

    if n == 0:
        return 1

    return n * fact(n-1)

if k < 0:
    print(0)
elif k > n:
    print(0)
else:
    print(fact(n)//(fact(k) * fact(n-k)))