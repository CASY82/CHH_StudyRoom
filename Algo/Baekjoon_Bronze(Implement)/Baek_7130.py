import sys

m, h = map(int, sys.stdin.readline().split())

n = int(sys.stdin.readline())

happiness = 0

for _ in range(n):
    c, b = map(int, sys.stdin.readline().split())

    happiness += max(m * c, h * b)

print(happiness)