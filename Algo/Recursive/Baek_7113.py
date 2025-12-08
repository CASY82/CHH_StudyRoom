import sys

n, m = map(int, sys.stdin.readline().split())

def square_divide(n, m):
    a, b = max(n, m), min(n, m)
    cnt = 0

    while b != 0:
        cnt += a // b
        a, b = b, a % b

    return cnt

print(square_divide(n, m))