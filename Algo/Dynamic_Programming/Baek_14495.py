import sys

n = int(sys.stdin.readline())
arr = [1, 1, 1] + [0 for _ in range(114)]

def func(n):
    if n <= 3:
        return 1
    elif arr[n] != 0:
        return arr[n]
    else:
        arr[n] = func(n - 1) + func(n - 3)
        return arr[n]

print(func(n))