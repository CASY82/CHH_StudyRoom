import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(n*2-1):
        if i == n-1:
            print("*", end='')
        else:
            if j == n - i - 1 or j == n + i - 1:
                print("*", end='')
            elif j > n + i - 1:
                continue
            else:
                print(" ", end='')

    print()