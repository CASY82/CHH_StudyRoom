import sys

k = int(sys.stdin.readline())
answer = 0

def power_of_two(k):
    result = 1
    base = 2

    while k > 0:
        if k % 2 == 1:
            result *= base
        base *= base
        k //= 2

    return result

tmp = power_of_two(k)
answer = tmp * (tmp - 1) // 2

print(bin(answer)[2:])