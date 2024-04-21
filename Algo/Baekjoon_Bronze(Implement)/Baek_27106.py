import sys

n = int(sys.stdin.readline())

tmp = 100 - n

# 25 10 5 1
cents = [0] * 4

size = [25, 10, 5, 1]

for cent in range(4):
    cents[cent] = tmp // size[cent]
    tmp %= size[cent]

print(*cents)