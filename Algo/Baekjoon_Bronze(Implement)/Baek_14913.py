import sys

a, d, k = map(int, sys.stdin.readline().split())

if (k - a) % d != 0:
    print("X")
else:
    result = ((k - a) // d) + 1

    if result > 0:
        print(result)
    else:
        print("X")