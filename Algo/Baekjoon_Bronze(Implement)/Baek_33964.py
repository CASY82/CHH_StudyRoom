import sys

x, y = map(int, sys.stdin.readline().split())

first = 0
second = 0

for i in range(x):
    first += 1 * (10 ** i)

for j in range(y):
    second += 1 * (10 ** j)

print(first + second)