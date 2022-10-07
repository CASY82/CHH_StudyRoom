import sys

n = int(sys.stdin.readline())
fibo = [0 for _ in range(n+1)]

#예의상 써준다
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    fibo[1] = 1
    fibo[2] = 1

    for i in range(3, n+1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n]

print(fibonacci(n), n-2)