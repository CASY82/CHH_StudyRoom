import sys

s0, n, m = map(int, sys.stdin.readline().split())
array = []

for _ in range(n + m):
    command = int(sys.stdin.readline())

    if command == 1:
        if s0 == len(array):
            s0 *= 2
            array.append(0)
        else:
            array.append(0)
    else:
        array.pop()

print(s0)