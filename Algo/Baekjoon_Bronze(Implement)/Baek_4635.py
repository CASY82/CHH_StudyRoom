import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    data = []
    result = 0
    last_time = 0

    for _ in range(n):
        miles, now_time = map(int, sys.stdin.readline().split())

        result += miles * (now_time - last_time)
        last_time = now_time

    print("{} miles".format(result))