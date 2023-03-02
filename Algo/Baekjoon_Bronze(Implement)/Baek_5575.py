import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

for time in (a, b, c):
    result = [0, 0, 0]

    for i in range(3):
        result[i] = time[i+3] - time[i]

    for i in range(2, 0, -1):
        if result[i] < 0:
            result[i-1] -= 1
            result[i] += 60

    print(*result)