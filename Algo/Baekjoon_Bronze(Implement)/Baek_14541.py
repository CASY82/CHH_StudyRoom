import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    result = 0
    last = 0
    for _ in range(n):
        speed, time = map(int, sys.stdin.readline().split())

        result += speed * (time-last)
        last = time

    print(result, "miles")