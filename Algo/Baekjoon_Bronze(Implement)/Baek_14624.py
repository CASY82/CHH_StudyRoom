import sys

n = int(sys.stdin.readline())

if n % 2 == 0:
    print("I LOVE CBNU")
else:
    for i in range(n):
        print("*", end='')
    print()

    for i in range(n//2+1):
        for j in range(n):
            if n // 2 + i < j:
                break
            if n // 2 - i == j or n // 2 + i == j:
                print("*", end='')
            else:
                print(" ", end='')
        print()