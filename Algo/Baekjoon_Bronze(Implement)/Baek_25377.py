import sys

n = int(sys.stdin.readline())
result = int(1e9)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a <= b:
        if result > b:
            result = b

if result == int(1e9):
    print(-1)
else:
    print(result)