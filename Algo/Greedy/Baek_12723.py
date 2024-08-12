import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n = int(sys.stdin.readline())

    x_array = list(map(int, sys.stdin.readline().split()))
    y_array = list(map(int, sys.stdin.readline().split()))

    x_array.sort()
    y_array.sort()

    res = 0

    for i in range(n):
        res += x_array[i] * y_array[n - i - 1]

    print("Case #{0}: {1}".format(case, res))