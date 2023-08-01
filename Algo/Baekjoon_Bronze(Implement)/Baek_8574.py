import sys
import math

n, k, x, y = map(int, sys.stdin.readline().split())

result = 0

for _ in range(n):
    cx, cy = map(int, sys.stdin.readline().split())

    distance = math.sqrt((cx - x) ** 2 + (cy - y) ** 2)

    if distance > k:
        result += 1

print(result)