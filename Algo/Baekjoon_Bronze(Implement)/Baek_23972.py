import sys

k, n = map(int, sys.stdin.readline().split())

if n == 1:
    print(-1)
else:
    result = (k*n) // (n-1)

    if (k * n) % (n - 1) != 0:
        result += 1

    print(result)