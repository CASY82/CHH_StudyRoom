import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    now = int(1e9)
    result = 0

    for _ in range(n):
        weight, cost = map(int, sys.stdin.readline().split())

        if now > (cost / weight):
            now = (cost / weight)
            result = cost
        elif now == (cost /weight):
            if result > cost : result = cost

    print(result)