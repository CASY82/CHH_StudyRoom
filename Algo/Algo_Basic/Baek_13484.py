import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
total = x

for _ in range(n):
    usage = int(sys.stdin.readline())

    total += x - usage

print(total)