import sys

n = int(sys.stdin.readline())

result = 0

for _ in range(n):
    horizon, vertical = map(int, sys.stdin.readline().split())

    if horizon == 136:
        result += 1000
    elif horizon == 142:
        result += 5000
    elif horizon == 148:
        result += 10000
    elif horizon == 154:
        result += 50000

print(result)