import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range((2 * n) - 1):
        if (((2 * n) - 1) // 2) + i == j or (((2 * n) - 1) // 2) - i == j:
            print("*", end="")
        elif (((2 * n) - 1) // 2) + i < j:
            continue
        else:
            print(" ", end="")
    if i < n-1:
        print()