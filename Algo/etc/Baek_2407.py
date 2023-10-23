import sys

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combination(n, k):
    if n < k:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

n, k = map(int, sys.stdin.readline().split())
result = combination(n, k)
print(result)