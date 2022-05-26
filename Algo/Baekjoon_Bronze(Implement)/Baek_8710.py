import sys

k, w, m = map(int, sys.stdin.readline().split())

result = 0

result = (w - k) // m

if (w - k) % m == 0:
    print(result)
else:
    print(result + 1)