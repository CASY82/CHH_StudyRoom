import sys
import math

n = int(sys.stdin.readline())

def is_square(x):
    if x < 0:
        return False
        # math.sqrt의 부동소수점 오차를 보정하기 위해 0.5를 더해 반올림
    r = int(math.sqrt(x) + 0.5)
    return r * r == x

def min_square(n):
    if is_square(n):
        return 1

    limit = int(math.sqrt(n))
    for i in range(1, limit + 1):
        if is_square(n - i * i):
            return 2

    m = n
    while m % 4 == 0:
        m /= 4

    if m % 8 == 7:
        return 4

    return 3

print(min_square(n))