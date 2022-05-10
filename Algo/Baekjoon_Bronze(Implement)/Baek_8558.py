import sys

n = int(sys.stdin.readline())
result = 1

if n < 5:
    for i in range(1, n+1):
        result *= i

    print(result % 10)
else:
    print(0)