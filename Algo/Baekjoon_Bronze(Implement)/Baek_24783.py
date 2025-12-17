import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())

    if a + b == c or max(a, b) - min(a, b) == c or a * b == c or max(a, b) / min(a, b) == c:
        print("Possible")
    else:
        print("Impossible")