import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    result = 0

    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())

        if a < 0 and b < 0 and c < 0:
            continue
        else:
            result += max(a, b, c)

    print(result)