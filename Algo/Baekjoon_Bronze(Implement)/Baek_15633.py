import sys

def find_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


n = int(sys.stdin.readline())
divisors = find_divisors(n)

print(sum(divisors) * 5 - 24)