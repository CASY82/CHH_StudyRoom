import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    result = 0

    for i in range(1, n+1):
        result += i * i

    print(result)