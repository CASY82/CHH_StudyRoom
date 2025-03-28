import sys

x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
min_distance = 1000000000000000
optimal = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    tmp = abs(x - a) + abs(y - b)
    if tmp < min_distance:
        min_distance = tmp

        if len(optimal) > 0:
            optimal.pop()

        optimal.append([a, b])

print(*optimal[0])